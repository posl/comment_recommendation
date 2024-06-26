def solve(n, k, a):
    ans = 0
    sum = 0
    right = 0
    for left in range(n):
        while (right < n and sum + a[right] < k):
            sum += a[right]
            right += 1
        ans += right - left
        if (right == left):
            right += 1
        else:
            sum -= a[left]
    return ans

if __name__ == '__main__':
    solve()