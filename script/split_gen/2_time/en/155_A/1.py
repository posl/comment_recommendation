def poor(A, B, C):
    if A == B and A != C:
        return True
    elif A == C and A != B:
        return True
    elif B == C and B != A:
        return True
    else:
        return False
