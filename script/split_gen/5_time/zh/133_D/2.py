def solve(n, a):
    s = sum(a)
    ans = []
    for i in range(n):
        ans.append(2*a[i] - s)
    return ans
