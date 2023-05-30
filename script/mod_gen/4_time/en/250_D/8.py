def solve(n):
    p = 1
    q = 2
    ans = 0
    while p < n:
        while p * q**3 < n:
            q += 1
        ans += q - 2
        p += 1
        q = p + 1
    return ans
n = int(input())
print(solve(n))
