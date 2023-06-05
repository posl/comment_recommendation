def solve(n, k, h):
    result = 0
    for i in range(0, n):
        if h[i] >= k:
            result += 1
    return result
