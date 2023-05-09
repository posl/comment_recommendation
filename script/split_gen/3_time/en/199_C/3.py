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
    S = list(S)
    #print(S)
    #print("".join(S))
    swap = 0
    for i in range(Q):
        if T[i] == 1:
            if swap == 0:
                S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
            else:
                if A[i] <= N:
                    if B[i] <= N:
                        S[A[i]-1+N], S[B[i]-1+N] = S[B[i]-1+N], S[A[i]-1+N]
                    else:
                        S[A[i]-1+N], S[B[i]-1-N] = S[B[i]-1-N], S[A[i]-1+N]
                else:
                    if B[i] <= N:
                        S[A[i]-1-N], S[B[i]-1+N] = S[B[i]-1+N], S[A[i]-1-N]
                    else:
                        S[A[i]-1-N], S[B[i]-1-N] = S[B[i]-1-N], S[A[i]-1-N]
        else:
            swap = 1 - swap
        #print("".join(S))
    if swap == 1:
        S = S[N:] + S[:N]
    print("".join(S))
