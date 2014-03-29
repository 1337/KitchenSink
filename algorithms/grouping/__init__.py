__author__ = 'brian'


"""Some of this was taken from
http://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/

(which means, this, however trivial it is, might be subject to copyright)
"""


from algorithms.geometry import Cluster, euclidean, calculate_center
import random

def kmeans(points, k, min_diff):
    """This was taken from
    http://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/

    (which means, this, however trivial it is, might be subject to copyright)
    """
    clusters = [Cluster([p], p, p.n) for p in random.sample(points, k)]

    while 1:
        plists = [[] for i in range(k)]

        for p in points:
            smallest_distance = float('Inf')
            for i in range(k):
                distance = euclidean(p, clusters[i].center)
                if distance < smallest_distance:
                    smallest_distance = distance
                    idx = i
            plists[idx].append(p)

        diff = 0
        for i in range(k):
            old = clusters[i]
            center = calculate_center(plists[i], old.n)
            new = Cluster(plists[i], center, old.n)
            clusters[i] = new
            diff = max(diff, euclidean(old.center, new.center))

        if diff < min_diff:
            break

    return clusters
