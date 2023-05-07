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
    S = list(S)
    for i in range(Q):
        if T[i] == 1:
            S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
        else:
            S = S[N:] + S[:N]
    print("".join(S))
