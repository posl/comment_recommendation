def main():
    S = input()
    n = len(S)
    Q = S.count('?')
    mod = 10**9+7
    ans = 0
    for i in range(n):
        if S[i] == 'B' or S[i] == '?':
            ans += pow(3,Q,mod)*pow(3,i,mod)*pow(2,n-1-i,mod)
            ans %= mod
        if S[i] == 'C' or S[i] == '?':
            ans += pow(3,Q,mod)*pow(3,i,mod)*pow(2,n-1-i,mod)
            ans %= mod
    print(ans)
