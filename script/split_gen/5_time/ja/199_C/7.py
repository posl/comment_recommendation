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
    S1 = S[:N]
    S2 = S[N:]
    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                S1 = S1[:A[i]-1] + S2[B[i]-N-1] + S1[A[i]:]
            else:
                S2 = S2[:A[i]-N-1] + S1[B[i]-1] + S2[A[i]-N:]
        else:
            S1, S2 = S2, S1
    print(S1+S2)
