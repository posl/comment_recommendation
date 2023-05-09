def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 10 ** 9
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            median = []
            for k in range(K):
                median += A[i + k][j : j + K]
            median.sort()
            ans = min(ans, median[K * K // 2])
    print(ans)

if __name__ == '__main__':
    main()