def main():
    S = input()
    Q = S.count('?')
    MOD = 10**9+7
    ans = 0
    for i in range(len(S)):
        if S[i] == 'C':
            ans += pow(3,Q,MOD)*pow(3,i,MOD)
            ans %= MOD
        elif S[i] == 'B':
            ans += pow(3,Q,MOD)*pow(3,i,MOD)
            ans %= MOD
            Q -= 1
        elif S[i] == 'A':
            ans += pow(3,Q,MOD)*pow(3,i,MOD)
            ans %= MOD
            Q -= 1
    print(ans)
main()
