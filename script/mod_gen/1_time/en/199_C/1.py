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
    ans = ''
    for i in range(Q):
        if T[i] == 1:
            if A[i] > N:
                A[i] = A[i] - N
            elif A[i] <= N:
                A[i] = A[i] + N
            if B[i] > N:
                B[i] = B[i] - N
            elif B[i] <= N:
                B[i] = B[i] + N
            S = S[:A[i]-1] + S[B[i]-1] + S[A[i]:B[i]-1] + S[A[i]-1] + S[B[i]:]
        elif T[i] == 2:
            S = S[N:] + S[:N]
    ans = S
    print(ans)

if __name__ == '__main__':
    main()