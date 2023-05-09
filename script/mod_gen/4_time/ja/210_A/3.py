def problem210_a():
    n, a, x, y = map(int, input().split())
    if n <= a:
        print(n * x)
    else:
        print(a * x + (n - a) * y)

if __name__ == '__main__':
    problem210_a()