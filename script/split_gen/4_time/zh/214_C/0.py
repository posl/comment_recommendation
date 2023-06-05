def solve(n, s, t):
    result = [0] * n
    for i in range(n):
        result[i] = t[i]
    for i in range(n - 1):
        if result[i + 1] > result[i] + s[i]:
            result[i + 1] = result[i] + s[i]
    for i in range(n):
        if result[i] > result[(i - 1) % n] + s[(i - 1) % n]:
            result[i] = result[(i - 1) % n] + s[(i - 1) % n]
    return result
