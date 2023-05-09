def solve(N, A, B):
    if A == 0 or B == 0:
        return 0
    return (N // (A + B)) * A + min(N % (A + B), A)
