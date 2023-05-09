def solve(n, a):
    ans = [0] * 10
    ans[a[0]] = 1
    ans[(a[0] + a[1]) % 10] += 1
    ans[(a[0] * a[1]) % 10] += 1
    for i in range(2, n):
        ans2 = [0] * 10
        for j in range(10):
            ans2[(j + a[i]) % 10] += ans[j]
            ans2[(j * a[i]) % 10] += ans[j]
        ans = ans2
    return ans
