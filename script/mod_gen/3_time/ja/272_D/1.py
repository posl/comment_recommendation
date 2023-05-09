def main():
    N, M = map(int, input().split())
    ans = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if (i - j) % 2 == 0:
                ans[i][j] = (i + j) // 2
            else:
                ans[i][j] = (i + j) // 2 + 1
    for i in range(N):
        print(*ans[i])

if __name__ == '__main__':
    main()