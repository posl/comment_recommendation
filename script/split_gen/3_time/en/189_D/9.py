def solve(n, s):
    if s[0] == "AND":
        ans = 2 ** (n - 1)
    else:
        ans = 2 ** n
    return ans
