def main():
    S = input()
    Q = S.count('?')
    MOD = 10**9 + 7
    A = [0] * (Q + 1)
    B = [0] * (Q + 1)
    C = [0] * (Q + 1)
    A[0] = B[0] = C[0] = 1
    for i in range(Q):
        A[i + 1] = A[i] * 3 % MOD
        B[i + 1] = B[i] * 3 % MOD
        C[i + 1] = C[i] * 3 % MOD
    ans = 0
    for i in range(len(S)):
        if S[i] == 'A':
            ans += B[Q] * C[Q]
            Q -= 1
        elif S[i] == 'B':
            ans += A[Q] * C[Q]
            Q -= 1
        elif S[i] == 'C':
            ans += A[Q] * B[Q]
            Q -= 1
        else:
            ans += A[Q] * B[Q] * 3
            ans += A[Q] * C[Q] * 3
            ans += B[Q] * C[Q] * 3
            Q -= 1
    print(ans % MOD)
