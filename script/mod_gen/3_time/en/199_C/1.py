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
    swich = 0
    for i in range(Q):
        if T[i] == 1:
            if swich == 0:
                if A[i] <= N and B[i] <= N:
                    S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
                elif A[i] <= N and B[i] > N:
                    S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:N] + S[A[i]-1] + S[N:B[i]-1] + S[N+A[i]-1] + S[B[i]:]
                elif A[i] > N and B[i] > N:
                    S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
            else:
                if A[i] <= N and B[i] <= N:
                    S = S[:N+A[i]-1] + S[N+B[i]-1] + S[N+A[i]:N+B[i]-1] + S[N+A[i]-1] + S[N+B[i]:]
                elif A[i] <= N and B[i] > N:
                    S = S[:N+A[i]-1] + S[N+B[i]-1] + S[N+A[i]:N] + S[N+A[i]-1] + S[N:N+B[i]-1] + S[A[i]-1] + S[N+B[i]:]
                elif A[i] > N and B[i] > N:
                    S = S[:N+A[i]-1] + S[N+B[i]-1] + S[N+A[i]:N+B[i]-1] + S[N+A[i]-1] + S[N+B[i]:]
        else:
            if swich == 0:
                swich = 1
            else:
                swich = 0
    if swich

if __name__ == '__main__':
    main()