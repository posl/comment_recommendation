def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(1, n):
        cnt += dfs(i, 1 << i, n, k, t)
    return cnt

if __name__ == '__main__':
    main()