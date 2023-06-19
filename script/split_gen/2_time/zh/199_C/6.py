def solve():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    reverse = False
    for i in range(Q):
        if T[i] == 1:
            if reverse:
                A[i] += N
                B[i] += N
                if A[i] > 2 * N:
                    A[i] -= 2 * N
                if B[i] > 2 * N:
                    B[i] -= 2 * N
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        else:
            reverse = not reverse
    if reverse:
        S = S[N:] + S[:N]
    print(S)
solve()
