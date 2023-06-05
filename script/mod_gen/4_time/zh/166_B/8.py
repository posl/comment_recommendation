def main():
    N,K = map(int,input().split())
    d = [0]*K
    A = []
    for i in range(K):
        d[i] = int(input())
        A.append(list(map(int,input().split())))
    S = [0]*N
    for i in range(K):
        for j in range(d[i]):
            S[A[i][j]-1] = 1
    print(S.count(0))

if __name__ == '__main__':
    main()