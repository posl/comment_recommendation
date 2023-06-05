def solve(n):
    ans = 0
    i = 1
    j = 1
    while i*j < n:
        if i < j:
            i += 1
        else:
            j += 1
        ans += 1
    return ans
