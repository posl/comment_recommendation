def solve(A, B, K):
    count = 0
    while A < B:
        A = A * K
        count = count + 1
    return count
