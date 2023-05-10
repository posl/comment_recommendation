def solve(A, B, K):
    cnt = 0
    while A < B:
        A *= K
        cnt += 1
    return cnt
