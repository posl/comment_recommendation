def main():
    n, a, x, y = input().split()
    n = int(n)
    a = int(a)
    x = int(x)
    y = int(y)
    if n <= a:
        print(n * x)
    else:
        print(a * x + (n - a) * y)

if __name__ == '__main__':
    main()