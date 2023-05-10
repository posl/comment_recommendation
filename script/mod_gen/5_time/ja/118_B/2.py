def main():
    n,m = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    cnt = [0] * (m + 1)
    for i in range(n):
        for j in range(1,a[i][0] + 1):
            cnt[a[i][j]] += 1
    ans = 0
    for i in range(m + 1):
        if cnt[i] == n:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()