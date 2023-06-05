def solve():
    S = input()
    mod = 10**9 + 7
    N = len(S)
    Q = S.count('?')
    S = S.replace('?','')
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] == 'B':
            ans += pow(3,Q,mod) * pow(3,i,mod)
        elif S[i] == 'C':
            ans += pow(3,Q,mod) * pow(3,i,mod) * 2
        ans %= mod
    print(ans)
