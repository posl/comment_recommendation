def main():
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
    for i in range(Q):
        if T[i] == 1:
            if A[i] < N and B[i] < N:
                S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
            elif A[i] < N and B[i] >= N:
                S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
            elif A[i] >= N and B[i] >= N:
                S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
            elif A[i] >= N and B[i] < N:
                S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
        elif T[i] == 2:
            S = S[N:] + S[:N]
    print(S)
