def solve(n,a):
    a.sort()
    ans = 1
    for i in range(n):
        if a[i] <= ans:
            ans += a[i]
        else:
            break
    return ans
