def main():
    n, a, x, y = map(int, input().split())
    if n > a:
        print(a * x + (n - a) * y)
    else:
        print(n * x)

if __name__ == '__main__':
    main()