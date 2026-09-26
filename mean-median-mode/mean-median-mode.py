from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """

    x = np.asarray(x, dtype=float)

    mean_x = np.mean(x)
    median_x = np.median(x)

    tally_x = Counter(x)
    top_freq = max(tally_x.values())

    smallest_key = min(k for k, v in tally_x.items() if v==top_freq)

    return dict(mean=float(mean_x), median=float(median_x), mode=float(smallest_key))
    