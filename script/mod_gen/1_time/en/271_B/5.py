def main():
    N, Q = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        L.append(list(map(int, input().split())))
        A.append(L[i][1:])
    S = []
    T = []
    for i in range(Q):
        S.append(int(input()))
        T.append(int(input()))
    for i in range(Q):
        print(A[S[i] - 1][T[i] - 1])

if __name__ == '__main__':
    main()