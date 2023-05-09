def solve(N, A):
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def f(i, j):
        if i == j:
            return 0
        elif i == j - 1:
            return A[i] ^ A[j]
        else:
            return min(f(i, k) ^ f(k + 1, j) for k in range(i, j))
    return f(0, N - 1)
