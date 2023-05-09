def check(S):
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
        return "Bad"
    else:
        return "Good"
S = input()
print(check(S))
