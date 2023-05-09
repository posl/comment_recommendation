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
    #print(N, S, Q, T, A, B)
    # 0: 1st half, 1: 2nd half
    half = 0
    for i in range(Q):
        if T[i] == 1:
            if half == 0:
                if A[i] <= N and B[i] <= N:
                    A[i] -= 1
                    B[i] -= 1
                    S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
                elif A[i] <= N and B[i] > N:
                    A[i] -= 1
                    B[i] -= N + 1
                    S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
                elif A[i] > N and B[i] <= N:
                    A[i] -= N + 1
                    B[i] -= 1
                    S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
                else:
                    A[i] -= N + 1
                    B[i] -= N + 1
                    S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
            else:
                if A[i] <= N and B[i] <= N:
                    A[i] -= 1
                    B[i] -= 1
                    S = S[:A[i]] + S[B[i]] + S[A[i]+1:B[i]] + S[A[i]] + S[B[i]+1:]
                elif A[i] <= N and B[i] > N:
                    A[i] -= 1
                    B[i] -= N + 1
                    S = S[:A[i]] + S[B[i]] + S[A[i]+1

if __name__ == '__main__':
    main()