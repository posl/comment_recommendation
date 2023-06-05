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
    rev = False
    for i in range(Q):
        if T[i] == 1:
            if rev:
                if A[i] <= N:
                    A[i] += N
                else:
                    A[i] -= N
                if B[i] <= N:
                    B[i] += N
                else:
                    B[i] -= N
            S = S[:A[i] - 1] + S[B[i] - 1] + S[A[i]:B[i] - 1] + S[A[i] - 1] + S[B[i]:]
        else:
            rev = not rev
    if rev:
        S = S[N:] + S[:N]
    print(S)
