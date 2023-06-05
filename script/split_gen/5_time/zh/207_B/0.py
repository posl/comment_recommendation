def solve(A,B,C,D):
    if A < B:
        return -1
    if D == 1:
        if A == C:
            return 0
        else:
            return -1
    if A <= C * D:
        return 1
    if A <= C * D + B:
        return 2
    return (A - C * D + B - C - 1) // (B - C) + 2
A,B,C,D = map(int, input().split())
print(solve(A,B,C,D))
