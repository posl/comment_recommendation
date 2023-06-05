def main():
    S = input()
    Q = S.count('?')
    mod = 10**9+7
    ans = 0
    for i in range(len(S)):
        if S[i]=='B' or S[i]=='?':
            ans += pow(3,Q,mod)*(S[:i].count('A')+S[i+1:].count('C'))
            ans %= mod
    print(ans)
main()
