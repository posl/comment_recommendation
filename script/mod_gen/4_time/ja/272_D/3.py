def main():
    N, M = map(int, input().split())
    if M == 1:
        print('\n'.join(' '.join(map(str, range(i, i + N))) for i in range(1, N * N + 1, N)))
        return
    ans = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                ans[i][j] = 0
            elif i == 0:
                ans[i][j] = ans[i][j - 1] + 1
            elif j == 0:
                ans[i][j] = ans[i - 1][j] + 1
            else:
                ans[i][j] = min(ans[i - 1][j], ans[i][j - 1]) + 1
    print('\n'.join(' '.join(map(str, ans[i])) for i in range(N)))

if __name__ == '__main__':
    main()