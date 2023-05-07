def main():
    S = input()
    MOD = 10 ** 9 + 7
    Q = S.count('?')
    ans = 0
    A = [0] * (Q + 1)
    B = [0] * (Q + 1)
    C = [0] * (Q + 1)
    for i in range(Q):
        A[i + 1] = pow(3, i, MOD)
        B[i + 1] = pow(3, i, MOD)
        C[i + 1] = pow(3, i, MOD)
    for i in range(Q):
        A[i + 1] = (A[i + 1] + A[i]) % MOD
        B[i + 1] = (B[i + 1] + B[i]) % MOD
        C[i + 1] = (C[i + 1] + C[i]) % MOD
    for i in range(len(S)):
        if S[i] == 'A':
            ans = (ans + B[Q - S[i + 1:].count('?')] + C[Q - S[i + 1:].count('?')]) % MOD
        elif S[i] == 'B':
            ans = (ans + A[Q - S[i + 1:].count('?')] + C[Q - S[i + 1:].count('?')]) % MOD
        elif S[i] == 'C':
            ans = (ans + A[Q - S[i + 1:].count('?')] + B[Q - S[i + 1:].count('?')]) % MOD
        elif S[i] == '?':
            ans = (ans + A[Q - S[i + 1:].count('?') - 1] + B[Q - S[i + 1:].count('?') - 1] + C[Q - S[i + 1:].count('?') - 1]) % MOD
    print(ans)
