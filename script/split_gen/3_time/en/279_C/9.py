def check_pattern(S, T):
    S = sorted(S)
    T = sorted(T)
    if S == T:
        return True
    else:
        return False
