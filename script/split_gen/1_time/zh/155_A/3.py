def answer(A,B,C):
    if A == B and B != C:
        return "是"
    elif A == C and B != C:
        return "是"
    elif B == C and A != B:
        return "是"
    else:
        return "否"
