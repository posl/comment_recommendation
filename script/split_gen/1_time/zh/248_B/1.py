def solve(a, b, k):
    ans = 0
    while a < b:
        a = a * k
        ans += 1
    return ans
