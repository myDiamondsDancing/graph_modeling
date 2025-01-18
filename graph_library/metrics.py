import math

import numpy as np
import scipy as sp


def cosine_similatiry(value1, value2) -> float:
    # Compute the dot product of the two vectors
    dot_product = np.dot(value1, value2)

    # Compute the norms of the vectors
    norm1 = np.linalg.norm(value1)
    norm2 = np.linalg.norm(value2)

    # Compute the cosine similarity
    cosine_similarity = dot_product / (norm1 * norm2)

    cosine_distance = (cosine_similarity + 1) / 2
    return cosine_distance


def reversed_cosine_similarity(value1, value2):
    return 2 * (1 - cosine_similatiry(value1, value2))


def reversed_kulback_leibler(value1, value2):
    return 1 - kulback_leibler(value1, value2)


def kulback_leibler(p, q):
    # Compute the normalized KL divergence
    kl = sp.special.kl_div(p, q).sum()
    normalized_divergence = 1 - (1 / (1 + kl))

    return normalized_divergence