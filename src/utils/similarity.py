from scipy.spatial import distance
from numpy import dot, linalg


def euclidean_distance(A, B):
    return distance.euclidean(A, B)


def cosine_similarity(A, B):
    # print(B)
    return dot(A, B) / (linalg.norm(A) * linalg.norm(B))
