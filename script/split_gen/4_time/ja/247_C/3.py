def solve(n):
    if n == 1:
        return [1]
    else:
        ans = solve(n-1)
        ans.append(n)
        ans += solve(n-1)
        return ans
