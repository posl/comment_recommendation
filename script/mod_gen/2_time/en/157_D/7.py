def main():
    n, m, k = map(int, input().split())
    friend = [[0] * n for _ in range(n)]
    block = [[0] * n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        friend[a - 1][b - 1] = 1
        friend[b - 1][a - 1] = 1
    for _ in range(k):
        c, d = map(int, input().split())
        block[c - 1][d - 1] = 1
        block[d - 1][c - 1] = 1
    ans = [0] * n
    for i in range(n):
        ans[i] = n - 1 - sum(friend[i]) - sum(block[i])
        for j in range(n):
            if friend[i][j] == 1:
                ans[i] -= 1
    for i in range(n):
        if friend[i][i] == 1:
            ans[i] += 1
    for i in range(n):
        print(ans[i], end = " ")
    print()

if __name__ == '__main__':
    main()