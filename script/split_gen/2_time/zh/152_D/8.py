def solve(n):
    ans = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if int(str(a)[-1]) == int(str(b)[0]) and int(str(a)[0]) == int(str(b)[-1]):
                ans += 1
    return ans
