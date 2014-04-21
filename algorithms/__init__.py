__author__ = 'brian'


def pick(objs, attrs):
    """From objs, return a list of dicts with only attrs preserved."""
    buffer = []
    for obj in objs:
        dct = {}
        for attr in attrs:
            try:
                dct[attr] = obj[attr]
            except KeyError:
                dct[attr] = obj.attr
            buffer.append(dct)
    return buffer
