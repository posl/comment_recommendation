def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = []
    A = []
    B = []
    for i in range(Q):
        T_i, A_i, B_i = map(int, input().split())
        T.append(T_i)
        A.append(A_i)
        B.append(B_i)
    
    S = list(S)
    for i in range(Q):
        if T[i] == 1:
            S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
        else:
            S[:N], S[N:] = S[N:], S[:N]
    print(''.join(S))
