def main():
    n, x = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(1, 1 << n):
        cnt = 1
        for j in range(n):
            if i >> j & 1:
                cnt *= a[j][0]
        if cnt == x:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()