def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        if i % 2 == 0:
            ans[0] += nums[i]
            ans[1] += nums[i]
        else:
            ans[0] -= nums[i]
            ans[1] -= nums[i]
    for i in range(1, n - 1):
        ans[i] = 2 * nums[i - 1] - ans[i - 1]
    print(' '.join(map(str, ans)))
solve()
