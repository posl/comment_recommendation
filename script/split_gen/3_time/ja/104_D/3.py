def main():
    S = input()
    Q = S.count('?')
    A = S.count('A')
    B = S.count('B')
    C = S.count('C')
    ans = 0
    for i in range(len(S)):
        if S[i] == 'A':
            A -= 1
        elif S[i] == 'B':
            B -= 1
        elif S[i] == 'C':
            C -= 1
        elif S[i] == '?':
            Q -= 1
            ans += (pow(3, Q, MOD) * (A * pow(3, B, MOD) + B * pow(3, C, MOD) + C * pow(3, A, MOD))) % MOD
            ans %= MOD
    print(ans)
