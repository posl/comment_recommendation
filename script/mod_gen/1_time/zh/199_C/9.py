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
        t = T[i]
        a = A[i]
        b = B[i]
        if t == 1:
            S = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
        elif t == 2:
            S = S[N:] + S[:N]
    print(S)

if __name__ == '__main__':
    main()