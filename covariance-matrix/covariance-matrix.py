import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    x = np.asarray(X, dtype=float)
    x_mean = np.mean(x, axis=0)
    print(x_mean, '\n')
    
    x_centered = x - x_mean
    print(x_centered, '\n')
    
    
    cov = (x_centered.T @ x_centered) / (len(x) - 1)
    
    print(cov, '\n')
    return cov
        
  




# X = [[1, 2], 
#      [2, 3], 
#      [3, 4]]

# covariance_matrix(X)

    