def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**9
    for i in range(N-K+1):
        for j in range(N-K+1):
            tmp = []
            for k in range(K):
                tmp += A[i+k][j:j+K]
            tmp.sort()
            ans = min(ans, tmp[K**2//2])
    print(ans)

if __name__ == '__main__':
    main()