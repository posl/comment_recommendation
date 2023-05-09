def solve(N, K, A):
    """
    :param N: int
    :param K: int
    :param A: list[int]
    :return: int
    """
    if N == K:
        return 1
    if N % K == 0:
        return 1
    return 2
