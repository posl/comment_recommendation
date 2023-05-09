def isYYMM(S):
    if int(S[2:]) <= 12 and int(S[2:]) >= 1:
        return True
    else:
        return False
