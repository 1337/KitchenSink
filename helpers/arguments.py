from functools import wraps
from inspect import getargspec

__author__ = 'brian'


from helpers.exceptions import ArgumentError


def get_arg_values(fn, args, kwargs):
    """returns a normalised arg_name: arg_value map.

    >>>def thing(a, b=1):
    >>>    print [x for x in a]
    >>>get_arg_values(thing, (1, 2))
    {'a': 1, 'b': 2}
    >>>get_arg_values(thing, None, {'a': 1, 'b': 2})
    {'a': 1, 'b': 2}
    """
    arg_map = {}
    original_fn_params = getargspec(fn)
    if original_fn_params.args:
        for arg in original_fn_params.args:  # arg is argument name
            if arg in kwargs:
                arg_map[arg] = kwargs[arg]
            else:
                arg_map[arg] = args[
                    original_fn_params.args.index(arg)]
    return arg_map


def type_check(**decorator_kwargs):
    """Raises ArgumentError if argument type mismatches.

    >>>@type_check(a=Iterable, b=int)
    >>>def thing(a):
    >>>    print [x for x in a]

    This function should return a decorator.
    """
    def complain(arg_name, expected_arg_type, got_arg_type):
        raise ArgumentError(
            "Expected argument {0} to be type {1}; got {2}".format(
                arg_name, expected_arg_type, got_arg_type))

    def decorator(fn):
        """This decorator should accept a function and return a
        replacement function.
        """
        @wraps(fn)
        def replacement_fn(*args, **kwargs):
            """This replacement for fn should accept the same arguments as
            fn, run fn (optional), and return the same type of arguments
            as fn.
            """
            derp = get_arg_values(fn, args, kwargs)
            for arg in derp:
                if not isinstance(derp[arg], decorator_kwargs[arg]):
                    complain(arg, decorator_kwargs[arg], type(derp[arg]))

            # function argumnet check succeeds
            return fn(*args, **kwargs)
        return replacement_fn
    return decorator


static = type_check  # alias


if __name__ == "__main__":
    from collections import Iterable

    @type_check(a=Iterable, b=int)
    def thing(a):
        print [x for x in a]

    thing([1])
    thing([1, 2, 3])
    thing(a=[1, 2, 3])
    try:
        thing(a=1)
    except ArgumentError:
        pass
    try:
        thing(False)
    except ArgumentError:
        pass
