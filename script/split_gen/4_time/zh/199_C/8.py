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
    for i in range(Q):
        if T[i] == 1:
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        else:
            S = S[N:] + S[:N]
    print(S)
