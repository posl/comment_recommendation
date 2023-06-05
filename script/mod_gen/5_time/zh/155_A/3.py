def is_triple_double(A, B, C):
    if A == B and B != C:
        return "是"
    elif B == C and C != A:
        return "是"
    elif C == A and A != B:
        return "是"
    else:
        return "否"

if __name__ == '__main__':
    is_triple_double()