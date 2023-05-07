def main():
    N, Q = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        L.append(tmp[0])
        A.append(tmp[1:])
    S = []
    T = []
    for i in range(Q):
        s, t = map(int, input().split())
        S.append(s)
        T.append(t)
    for i in range(Q):
        print(A[S[i]-1][T[i]-1])

if __name__ == '__main__':
    main()