import numpy as np


def expand(matrix: np.ndarray, rows: int = 1, columns: int = 1) -> np.ndarray:
    return np.pad(
        matrix,
        # add 0 rows above, 1 row below, 0 columns at left, 1 column at right
        ((0, 1), (0, 1)),
        mode='constant',
        constant_values=0
    )