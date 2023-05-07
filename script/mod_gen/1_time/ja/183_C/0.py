def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i == j == k:
                    continue
                if T[i][j] + T[j][k] == K:
                    ans += 1
    print(ans // 2)

if __name__ == '__main__':
    main()