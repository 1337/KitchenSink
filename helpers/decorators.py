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
    >>>a.foo()
    ...
    """
    def decorator(fn):
        fn = types.MethodType(fn, instance, instance.__class__)
        setattr(instance, fn.func_name, fn)
        return fn
    return decorator
