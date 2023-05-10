def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = [0] * m
    for i in range(n):
        for j in range(1, a[i][0] + 1):
            ans[a[i][j] - 1] += 1
    print(ans.count(n))

if __name__ == '__main__':
    main()