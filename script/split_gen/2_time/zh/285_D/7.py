def is_changeable(S,T):
    if S == T:
        return False
    if len(S) != len(T):
        return False
    if S[0] == T[-1]:
        return False
    if T[0] == S[-1]:
        return False
    return True
