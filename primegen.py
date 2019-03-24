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


def gen_prime_list(n):
    """
    Generate a list of primes
    :param n: the maximum size of the largest prime (not inclusive)
    :return: a list of primes
    """

    prime_list = []
    A = gen_lookup_table(n)
    for i in range(n):
        if A[i]:
            prime_list.append(i)

    return prime_list
