def main():
    S = input()
    Q = S.count('?')
    A = [0] * (Q + 1)
    B = [0] * (Q + 1)
    C = [0] * (Q + 1)
    for i, c in enumerate(S):
        if c == 'A':
            A[Q - i] += 1
        elif c == 'B':
            B[Q - i] += 1
        elif c == 'C':
            C[Q - i] += 1
        elif c == '?':
            A[Q - i] += 1
            B[Q - i] += 1
            C[Q - i] += 1
        A[Q - i - 1] += A[Q - i]
        B[Q - i - 1] += B[Q - i]
        C[Q - i - 1] += C[Q - i]
    ans = 0
    for i in range(Q + 1):
        ans += A[i] * B[i] * C[i]
        ans %= 10**9 + 7
    print(ans)
main()
