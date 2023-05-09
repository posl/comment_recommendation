def solution(x, a, d, n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if d == 0:
        return abs(x - a)
    else:
        if (x - a) % d == 0:
            return abs((x - a) // d)
        else:
            return min(abs((x - a) // d) + (x - a) % d, abs((x - a) // d + 1) - (x - a) % d)
