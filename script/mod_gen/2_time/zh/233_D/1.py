def solve(n, k, a):
    ans = 0
    sum = 0
    right = 0
    for left in range(n):
        while right < n and sum < k:
            sum += a[right]
            right += 1
        if sum < k:
            break
        ans += n - right + 1
        if right == left:
            right += 1
        else:
            sum -= a[left]
    return ans

if __name__ == '__main__':
    solve()