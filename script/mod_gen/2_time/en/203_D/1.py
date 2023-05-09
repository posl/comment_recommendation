def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**9
    for i in range(N-K+1):
        for j in range(N-K+1):
            arr = []
            for m in range(K):
                arr += A[i+m][j:j+K]
            arr.sort()
            ans = min(ans, arr[K*K//2])
    print(ans)

if __name__ == '__main__':
    main()