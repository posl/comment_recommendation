def isRotated(S, T):
    if S == T:
        return "Yes"
    else:
        for i in range(len(S)-1):
            S = S[-1] + S[:-1]
            if S == T:
                return "Yes"
        return "No"
