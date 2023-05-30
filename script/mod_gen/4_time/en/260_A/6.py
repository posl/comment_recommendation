def problem():
    S = input()
    S = list(S)
    for i in range(0, len(S)):
        if S.count(S[i]) == 1:
            print(S[i])
            return
    print(-1)
problem()
