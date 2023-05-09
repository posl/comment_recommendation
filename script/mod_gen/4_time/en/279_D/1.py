def solve(A: int, B: int):
    import math
    g = 1
    result = A
    while True:
        t = A / math.sqrt(g)
        if result < t + B:
            break
        result = t + B
        g += 1
    return result

if __name__ == '__main__':
    solve()