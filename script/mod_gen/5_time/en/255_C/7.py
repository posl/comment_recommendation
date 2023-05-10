def solution(x, a, d, n):
    if n == 1:
        return 0
    elif d == 0:
        return abs(x - a)
    else:
        if n % 2 == 0:
            return abs(x - a - (n // 2) * d)
        else:
            return min(abs(x - a - (n // 2) * d), abs(x - a - (n // 2 - 1) * d - d))

if __name__ == '__main__':
    solution()