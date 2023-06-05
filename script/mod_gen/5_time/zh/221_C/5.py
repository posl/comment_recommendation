def f(n):
    s = str(n)
    ans = 0
    for i in range(1, len(s)):
        a = int(s[:i])
        b = int(s[i:])
        ans = max(ans, a * b)
    return ans
n = int(input())
print(f(n))
