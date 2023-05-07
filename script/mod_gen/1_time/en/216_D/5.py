def solve():
    n, m = map(int, input().split())
    k = [int(input()) for _ in range(m)]
    a = [list(map(int, input().split())) for _ in range(m)]
    cnt = [0] * (n + 1)
    for i in range(m):
        for j in range(k[i]):
            cnt[a[i][j]] += 1
    for i in range(1, n + 1):
        if cnt[i] != 2:
            print('No')
            return
    print('Yes')
solve()

if __name__ == '__main__':
    solve()