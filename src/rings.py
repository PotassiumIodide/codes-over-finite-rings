import numpy as np
from typing import List

from .nary import all_nary

def Z(m: int, n: int) -> List[np.ndarray]:
    """
    Return the list of all n-tuple vectors in a ring Zm.
    Arguments:
    m: {int} - the modulo of the ring of integers
    n: {int} - the length (or dimension) of tuple
    Returns:
    {List[numpy.ndarray]} - The list of all n-tuple vectors in Zm
    """
    return [np.array(v) for v in all_nary(m, n)]