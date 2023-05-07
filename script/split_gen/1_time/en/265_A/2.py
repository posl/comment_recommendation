def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(x * (n // 3))
    elif n % 3 == 1:
        print(min(x + y, y * (n // 3) + x))
    else:
        print(min(x * (n // 3 + 1), y * (n // 3 + 1) - x))
main()
