from functools import wraps

__author__ = 'brian'


import types


def decorator_decorator(**decorator_kwargs):
    """This function should return a decorator."""
    def decorator(fn):
        """This decorator should accept a function and return a
        replacement function.
        """
        def replacement_fn(*args, **kwargs):
            """This replacement for fn should accept the same arguments as
            fn, run fn (optional), and return the same type of arguments
            as fn.
            """
            return fn(*args, **kwargs)
        return replacement_fn
    return decorator



def patch_class(instance):
    """Modified from https://wiki.python.org/moin/PythonDecoratorLibrary

    >>>class A():
    >>>    pass
    >>>a = A()
    >>>
    >>>@patch_class(a)
    >>>def foo(self):
    >>>    print self
    >>>
    >>>a.foo()  # a now has foo()
    ...
    """
    def decorator(fn):
        fn = types.MethodType(fn, instance, instance.__class__)
        setattr(instance, fn.func_name, fn)
        return fn
    return decorator


def deferred(fn):
    """This function will exit before it completes.

    >>>@deferred
    >>>def poop():
    >>>    # long computation
    >>>
    >>>poop()
    """
    import threading

    class TaskFinished(object):
        thread = None
        done_fns = []
        fail_fns = []

        def __init__(self, thread):
            self.thread = thread
            try:
                wat = self.thread.join()
            except BaseException as err:
                for fn in self.fail_fns:
                    fn(err)
            else:
                for fn in self.done_fns:
                    fn(wat)

        def __getattr__(self, item):
            return getattr(self.thread, item)

        def done(self, fn):
            self.done_fns.append(fn)
            return self

        def fail(self, fn):
            self.fail_fns.append(fn)
            return self

    def replacement_fn(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return TaskFinished(thread)

    return replacement_fn


def asap(fn):
    """Runs the function right here and now.

    Oh, guess what? It's already running as soon as possible.

    Fuck you, managers.
    """
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapped

this_is_urgent = quickly = asap


if __name__ == '__main__':
    @deferred
    def hello():
        print "hello"

    def cb():
        print "world"

    res = hello()
    res.done(cb)
