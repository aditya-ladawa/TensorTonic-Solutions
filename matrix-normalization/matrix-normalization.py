import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
  """
  Returns a NumPy array with the same shape as matrix.
  """
  m = np.asarray(matrix, dtype=float)
  
  if norm_type == 'l1':
    l1norm = np.sum(np.abs(m), axis=axis, keepdims=True)
    l1norm = np.where(l1norm == 0, 1.0, l1norm)
    print(l1norm, '\n')
    norm = m / l1norm

  if norm_type == 'l2':
    l2norm = np.sqrt(np.sum(np.power(m, 2), axis=axis, keepdims=True))
    l2norm = np.where(l2norm == 0, 1.0, l2norm)
    print(l2norm, '\n')
    norm = m / l2norm
    
  if norm_type == 'max':
    maxnorm = np.max(np.abs(m), axis=axis, keepdims=True)
    maxnorm = np.where(maxnorm == 0, 1.0, maxnorm)
    print(maxnorm, '\n')
    norm = m / maxnorm

  return norm


    