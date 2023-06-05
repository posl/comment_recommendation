def solve(a, b, t):
    result = 0
    for i in range(1, t+1):
        if i % a == 0:
            result += b
    return result
