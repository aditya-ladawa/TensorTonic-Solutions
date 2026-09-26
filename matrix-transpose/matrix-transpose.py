import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    a = np.asarray(A, dtype=float)
    n, m = a.shape

    t = np.zeros((m, n), dtype=float)

    for i in range(n):
        for j in range(m):
            t[j][i] = a[i][j] 

    return t
