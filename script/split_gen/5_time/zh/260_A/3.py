def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2]:
        print(-1)
    elif S[0] != S[1] and S[1] == S[2]:
        print(S[0])
    elif S[0] == S[1] and S[1] != S[2]:
        print(S[2])
    elif S[0] != S[1] and S[1] != S[2] and S[0] == S[2]:
        print(S[1])
    else:
        print(-1)
