def solve(A, B, K):
    if A == 0:
        return 'b' * B
    if B == 0:
        return 'a' * A
    if K <= comb(A + B - 1, A - 1):
        return 'a' + solve(A - 1, B, K)
    else:
        return 'b' + solve(A, B - 1, K - comb(A + B - 1, A - 1))
