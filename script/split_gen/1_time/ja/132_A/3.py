def main():
    S = input()
    S = list(S)
    S.sort()
    if S[0] == S[1] and S[2] == S[3]:
        print("Yes")
    else:
        print("No")
