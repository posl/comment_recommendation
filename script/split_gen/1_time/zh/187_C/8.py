def solve():
    N = int(input())
    S = [input() for i in range(N)]
    S = [s[1:] if s[0] == '!' else s for s in S]
    S.sort()
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            print(S[i])
            return
    print('satisfiable')
