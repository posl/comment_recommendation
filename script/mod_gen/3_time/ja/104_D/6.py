def main():
    S = input()
    Q = S.count('?')
    Q3 = pow(3, Q, 10**9+7)
    A = [0] * len(S)
    B = [0] * len(S)
    C = [0] * len(S)
    for i, s in enumerate(S):
        if s == 'A':
            A[i] = 1
        elif s == 'B':
            B[i] = 1
        elif s == 'C':
            C[i] = 1
    for i in range(1, len(S)):
        A[i] += A[i-1]
        B[i] += B[i-1]
        C[i] += C[i-1]
    ans = 0
    for i, s in enumerate(S):
        if s == '?':
            ans += A[i-1] * B[i-1] * (Q3 // 3) % (10**9+7)
            ans += A[i-1] * C[i-1] * (Q3 // 3) % (10**9+7)
            ans += B[i-1] * C[i-1] * (Q3 // 3) % (10**9+7)
            ans %= 10**9+7
    print(ans)
main()
