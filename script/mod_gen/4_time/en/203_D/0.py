def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 10 ** 9
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            B = []
            for k in range(K):
                for l in range(K):
                    B.append(A[i + k][j + l])
            B.sort()
            ans = min(ans, B[(K * K) // 2])
    print(ans)

if __name__ == '__main__':
    main()