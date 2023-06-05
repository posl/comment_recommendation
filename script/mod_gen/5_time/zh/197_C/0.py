def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1 << 30
    for i in range(n):
        x = 0
        for j in range(i, n):
            x |= a[j]
            y = 0
            for k in range(j + 1, n):
                y ^= a[k]
                ans = min(ans, x + y)
    print(ans)

if __name__ == '__main__':
    solve()