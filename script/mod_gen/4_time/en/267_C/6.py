def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            b = a[i:j+1]
            if len(b) > m:
                continue
            ans = max(ans, sum([x * (j-i+1) for x in b]))
    print(ans)

if __name__ == '__main__':
    solve()