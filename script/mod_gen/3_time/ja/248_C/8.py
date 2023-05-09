def solve(N, M, K):
    if N * M < K:
        return 0
    if N > K:
        return 0
    if N == K:
        return 1
    if N == 1:
        return 1
    if M == 1:
        return 1
    if N == 2:
        return M
    if M == 2:
        return N
    return 0

if __name__ == '__main__':
    solve()