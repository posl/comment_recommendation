def solve(S):
    if S[0] < 'A' or S[0] > 'Z':
        return "No"
    if S[-1] < 'A' or S[-1] > 'Z':
        return "No"
    if len(S) != 8:
        return "No"
    if S[1:7] < '100000' or S[1:7] > '999999':
        return "No"
    return "Yes"
