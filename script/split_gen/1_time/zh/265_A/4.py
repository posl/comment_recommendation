def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(n // 3 * y)
    else:
        if n % 3 == 1:
            print((n // 3 * y) + x)
        else:
            print((n // 3 * y) + y)
