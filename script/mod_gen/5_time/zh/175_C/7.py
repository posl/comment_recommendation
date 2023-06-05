def problem175_c():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= d * k:
        print(x - d * k)
        return
    n = x // d
    if (k - n) % 2 == 0:
        print(x - n * d)
    else:
        print(d - x + n * d)

if __name__ == '__main__':
    problem175_c()