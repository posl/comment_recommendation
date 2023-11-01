def solve():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S_set = set(S)
    for i in range(N):
        if '!' + S[i] in S_set:
            print(S[i])
            return
