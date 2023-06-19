def is_split(S):
    if S[0] == "0":
        return False
    if S[1] == "0" and S[2] == "0":
        return False
    if S[3] == "0" and S[4] == "0" and S[5] == "0" and S[6] == "0":
        return False
    if S[7] == "0" and S[8] == "0":
        return False
    if S[9] == "0" and S[8] == "0" and S[7] == "0":
        return False
    return True
S = input()
