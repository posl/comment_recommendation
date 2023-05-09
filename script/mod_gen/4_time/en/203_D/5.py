def main():
    N,K = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    A.sort()
    A = list(map(list, zip(*A)))
    A.sort()
    A = list(map(list, zip(*A)))
    ans = 10**9
    for i in range(N-K+1):
        for j in range(N-K+1):
            tmp = []
            for k in range(i, i+K):
                for l in range(j, j+K):
                    tmp.append(A[k][l])
            tmp.sort()
            ans = min(ans, tmp[(K*K)//2])
    print(ans)

if __name__ == '__main__':
    main()