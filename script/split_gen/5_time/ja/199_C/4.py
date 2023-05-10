def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0]*Q
    A = [0]*Q
    B = [0]*Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    #print(N, S, Q, T, A, B)
    #print(N, S, Q, T, A, B)
    S1 = S[:N]
    S2 = S[N:]
    #print(S1, S2)
    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                S1 = S1[:A[i]-1] + S2[B[i]-1] + S1[A[i]:]
            elif A[i] > N:
                S2 = S2[:A[i]-N-1] + S1[B[i]-1] + S2[A[i]-N:]
        elif T[i] == 2:
            S1, S2 = S2, S1
        #print(S1, S2)
    print(S1+S2)
main()
