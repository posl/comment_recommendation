def main():
    #n, a, x, y = map(int, input().split())
    n, a, x, y = 5, 3, 20, 15
    if n > a:
        print(a * x + (n - a) * y)
    else:
        print(n * x)

if __name__ == '__main__':
    main()