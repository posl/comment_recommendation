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
    a = list(S[:N])
    b = list(S[N:])
    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                a[A[i]-1], a[B[i]-1] = a[B[i]-1], a[A[i]-1]
            else:
                b[A[i]-N-1], b[B[i]-N-1] = b[B[i]-N-1], b[A[i]-N-1]
        elif T[i] == 2:
            a, b = b, a
    print("".join(a+b))

if __name__ == '__main__':
    main()