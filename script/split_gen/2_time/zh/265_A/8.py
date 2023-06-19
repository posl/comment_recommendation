def solve(x, y, n):
    ans = 0
    while n > 0:
        if n >= 3:
            if x * 3 > y:
                ans += y
                n -= 3
            else:
                ans += x
                n -= 1
        else:
            ans += x
            n -= 1
    return ans
x, y, n = map(int, input().split())
print(solve(x, y, n))
