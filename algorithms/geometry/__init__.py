__author__ = 'brian'


"""Some of this was taken from
http://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/

(which means, this, however trivial it is, might be subject to copyright)
"""


from collections import namedtuple
from math import sqrt


Point = namedtuple('Point', ('coords', 'n', 'ct'))
Cluster = namedtuple('Cluster', ('points', 'center', 'n'))

def euclidean(p1, p2):
    """This was taken from
    http://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/

    (which means, this, however trivial it is, might be subject to copyright)
    """
    return sqrt(sum([
        (p1.coords[i] - p2.coords[i]) ** 2 for i in range(p1.n)
    ]))


def calculate_center(points, n):
    """This was taken from
    http://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/

    (which means, this, however trivial it is, might be subject to copyright)
    """
    vals = [0.0 for i in range(n)]
    plen = 0
    for p in points:
        plen += p.ct
        for i in range(n):
            vals[i] += (p.coords[i] * p.ct)
    return Point([(v / plen) for v in vals], n, 1)
