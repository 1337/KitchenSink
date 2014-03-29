from functools import partial

__author__ = 'brian'


def strip_ord(string, max=128):
    """Remove characters higher than (max) in int."""
    return ''.join([x for x in string if ord(x) < max])


strip_unicode6 = partial(strip_ord, max=67108864)
strip_unicode5 = partial(strip_ord, max=2097152)
strip_unicode4 = partial(strip_ord, max=65536)
strip_unicode3 = partial(strip_ord, max=2048)
strip_unicode2 = partial(strip_ord, max=128)  # i.e. keep ascii



def dominant_color(image):
    """
    :param {Image} image
    """
    try:
        import Image
    except ImportError:
        try:
            from PIL import Image
        except ImportError as err:
            raise ImportError("PIL (or Pillow) package required to run "
                              "dominant_color.")

