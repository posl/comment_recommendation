def is_cute(A, B, C):
    if A == B and A != C:
        return True
    if B == C and B != A:
        return True
    if C == A and C != B:
        return True
    return False
A, B, C = map(int, input().split())
