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
    for i in range(Q):
        if T[i] == 1:
            if A[i] > N:
                a = A[i] - N
            else:
                a = A[i] + N
            if B[i] > N:
                b = B[i] - N
            else:
                b = B[i] + N
            S = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
        else:
            S = S[N:] + S[:N]
    print(S)
