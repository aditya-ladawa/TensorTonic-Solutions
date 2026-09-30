import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x = np.asarray(x, dtype=float)
    x_mean = np.sum(x) / len(x)
    print(x_mean)

    cnt = 0

    for i in x:
      cnt += (i - x_mean)**2
    print(cnt)

    sample_variance = (cnt / (len(x) - 1))
    print(sample_variance)
    sample_std = (np.sqrt(sample_variance))
    print(sample_std)

    return {"variance": float(sample_variance), "standard_deviation": float(sample_std)}

