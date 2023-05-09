def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    sum = 0
    r = 0
    for l in range(n):
        while r < n and sum < k:
            sum += a[r]
            r += 1
        if sum < k:
            break
        ans += n - r + 1
        sum -= a[l]
    print(ans)

if __name__ == '__main__':
    solve()