def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = float("inf")
    left = 0
    right = s
    for i in range(n-1):
        left += a[i]
        right -= a[i]
        ans = min(ans, abs(left-right))
    print(ans)
    return 0

if __name__ == '__main__':
    solve()