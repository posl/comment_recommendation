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
    flag = 0
    S1 = S[:N]
    S2 = S[N:]
    for i in range(Q):
        if T[i] == 1:
            if flag == 0:
                if A[i] <= N and B[i] <= N:
                    S1 = S1[:A[i]-1] + S2[B[i]-1] + S1[A[i]:]
                    S2 = S2[:B[i]-1] + S[S1.index(S2[B[i]-1])] + S2[B[i]:]
                elif A[i] > N and B[i] > N:
                    S2 = S2[:A[i]-N-1] + S1[B[i]-N-1] + S2[A[i]-N:]
                    S1 = S1[:B[i]-N-1] + S[S2.index(S1[B[i]-N-1])] + S1[B[i]-N:]
                elif A[i] <= N and B[i] > N:
                    S1 = S1[:A[i]-1] + S2[B[i]-N-1] + S1[A[i]:]
                    S2 = S2[:B[i]-N-1] + S[S1.index(S2[B[i]-N-1])] + S2[B[i]-N:]
                elif A[i] > N and B[i] <= N:
                    S2 = S2[:A[i]-N-1] + S1[B[i]-1] + S2[A[i]-N:]
                    S1 = S1[:B[i]-1] + S[S2.index(S1[B[i]-1])] + S1[B[i]:]
            else:
                if A[i] <= N and B[i] <= N:
                    S2 = S2[:A[i]-1] + S1[B[i]-1] + S2[A[i]:]
                    S1 = S1[:B[i]-1] + S[S2.index(S1[B[i]-1])] + S1[B[i]:]
                elif A[i] >
