def check_pattern(S, T):
    for i in range(len(S)):
        if S[i] != T[i]:
            return False
    return True
