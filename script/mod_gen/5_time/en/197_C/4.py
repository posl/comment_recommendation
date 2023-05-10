def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1 << 30
    for i in range(n):
        x = 0
        for j in range(i, n):
            x |= a[j]
            ans = min(ans, x)
    print(ans)

if __name__ == '__main__':
    solve()