def check_string(S):
    if len(S) != 10:
        return False
    if S[0].isupper() and S[9].isupper():
        if S[1:7].isdigit() and 100000 <= int(S[1:7]) <= 999999:
            return True
    return False
