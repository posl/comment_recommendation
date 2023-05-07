def main():
    S = input()
    K = int(input())
    N = len(S)
    if N == 1:
        print(S)
        return
    if N == 2:
        if S[0] == S[1]:
            print(S[0])
        else:
            print(S[1])
        return
    if S[0] == S[1]:
        if S[1] == S[2]:
            print(S[0])
        else:
            print(S[2])
    else:
        print(S[1])
