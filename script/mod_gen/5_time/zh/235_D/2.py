def solve(a, n):
    if a == 1:
        return n-1
    ans = 0
    while n > 0:
        if n % a == 0:
            n /= a
            ans += 1
        else:
            ans += n % a
            n -= n % a
    return ans
a, n = map(int, input().split())
print(solve(a, n))
