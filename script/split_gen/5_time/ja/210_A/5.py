def solve():
    #n, a, x, y = map(int, input().split())
    n, a, x, y = map(int, input().split())
    if n <= a:
        print(n * x)
    else:
        print(a * x + (n - a) * y)
