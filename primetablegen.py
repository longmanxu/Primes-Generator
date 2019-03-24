import primelookupgen


def gen_prime_list(n):
    """
    Generate a list of primes
    :param n: the maximum size of the largest prime (not inclusive)
    :return: a list of primes
    """

    prime_list = []
    A = primelookupgen.gen_lookup_table(n)
    for i in range(n):
        if A[i]:
            prime_list.append(i)

    return prime_list
