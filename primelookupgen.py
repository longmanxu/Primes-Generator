import math


def gen_lookup_table(n):
    """
    Generates and returns a lookup table of primes up to n

    :param int n: the length of the lookup table
    :return: the lookup table
    """

    A = [True for _ in range(n)]

    A[0] = A[1] = False

    for i in range(2, math.ceil(math.sqrt(n))):
        if not A[i]:
            continue
        else:
            for j in range(i*i, n, i):
                A[j] = False

    return A
