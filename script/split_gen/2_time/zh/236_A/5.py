def solve(a, n):
    if n < a:
        return -1
    if n == a:
        return 1
    if n % a == 0:
        return -1
    s = str(n)
    for i in range(1, len(s)):
        x = int(s[i:] + s[:i])
        if x % a == 0:
            return i + 1
    return -1
