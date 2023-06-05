def solve(n, k, a):
    ans = 0
    s = 0
    right = 0
    for left in range(n):
        while right < n and s + a[right] < k:
            s += a[right]
            right += 1
        ans += right - left
        s -= a[left]
    return ans

if __name__ == '__main__':
    solve()