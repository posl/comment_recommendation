def solve():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0] * Q
    A = [0] * Q
    B = [0] * Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    #print(N, S, Q, T, A, B)
    S1 = S[0:N]
    S2 = S[N:2*N]
    #print(S1, S2)
    for i in range(Q):
        if T[i] == 2:
            S1, S2 = S2, S1
        else:
            if A[i] - 1 < N:
                if B[i] - 1 < N:
                    S1 = S1[0:A[i]-1] + S2[B[i]-1] + S1[A[i]:B[i]-1] + S2[A[i]-1] + S1[B[i]:]
                else:
                    S1 = S1[0:A[i]-1] + S2[A[i]-1] + S1[A[i]:]
                    S2 = S2[0:B[i]-N-1] + S1[B[i]-N-1] + S2[B[i]-N:B[i]-1] + S1[B[i]-1] + S2[B[i]:]
            else:
                S2 = S2[0:A[i]-N-1] + S1[A[i]-N-1] + S2[A[i]-N:A[i]-1] + S1[A[i]-1] + S2[A[i]:]
                S1 = S1[0:B[i]-1] + S2[B[i]-1] + S1[B[i]:]
        #print(S1, S2)
    print(S1 + S2)

if __name__ == '__main__':
    solve()