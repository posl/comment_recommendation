def find_min_x(n):
    if n == 0:
        return 0
    for i in range(1, 1000000):
        x = n + i
        if x >= n and x >= 0:
            for a in range(1, 1000000):
                if a ** 3 + a ** 2 * a + a * a * a + a * a * a >= x:
                    break
                for b in range(1, 1000000):
                    if a ** 3 + a ** 2 * b + a * b * b + b * b * b == x:
                        return x
                    elif a ** 3 + a ** 2 * b + a * b * b + b * b * b > x:
                        break
    return -1

if __name__ == '__main__':
    find_min_x()