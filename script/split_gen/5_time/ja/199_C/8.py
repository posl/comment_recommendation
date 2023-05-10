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
    #print(N)
    #print(S)
    #print(Q)
    #print(T)
    #print(A)
    #print(B)
    S1 = S[:N]
    S2 = S[N:]
    for i in range(Q):
        if T[i] == 1:
            if A[i] < N and B[i] < N:
                tmp = S1[A[i]]
                S1 = S1[:A[i]] + S1[B[i]] + S1[A[i]+1:]
                S1 = S1[:B[i]] + tmp + S1[B[i]+1:]
            elif A[i] < N and B[i] >= N:
                tmp = S1[A[i]]
                S1 = S1[:A[i]] + S2[B[i]-N] + S1[A[i]+1:]
                S2 = S2[:B[i]-N] + tmp + S2[B[i]-N+1:]
            elif A[i] >= N and B[i] < N:
                tmp = S2[A[i]-N]
                S2 = S2[:A[i]-N] + S1[B[i]] + S2[A[i]-N+1:]
                S1 = S1[:B[i]] + tmp + S1[B[i]+1:]
            elif A[i] >= N and B[i] >= N:
                tmp = S2[A[i]-N]
                S2 = S2[:A[i]-N] + S2[B[i]-N] + S2[A[i]-N+1:]
                S2 = S2[:B[i]-N] + tmp + S2[B[i]-N+1:]
        elif T[i] == 2:
            S1, S2 = S2, S1
    S = S1 + S2
    print(S)
