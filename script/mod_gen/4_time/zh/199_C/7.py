def main():
    N = int(input())
    S = list(input())
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
            S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
        elif T[i] == 2:
            S = S[N:] + S[:N]
    print(''.join(S))

if __name__ == '__main__':
    main()