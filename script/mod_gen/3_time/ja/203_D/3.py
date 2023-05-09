def main():
    N, K = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    ans = 10**9
    for i in range(N-K+1):
        for j in range(N-K+1):
            B = []
            for k in range(i, i+K):
                for l in range(j, j+K):
                    B.append(A[k][l])
            B.sort()
            ans = min(ans, B[(K**2)//2])
    print(ans)

if __name__ == '__main__':
    main()