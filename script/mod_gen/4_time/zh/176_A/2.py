def problems176_a():
    n, x, t = map(int, input().split())
    if n % x == 0:
        print(int(n / x * t))
    else:
        print(int((n / x + 1) * t))

if __name__ == '__main__':
    problems176_a()