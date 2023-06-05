def main():
    x, y = map(int, input().split())
    n = 0
    while x * n < y:
        n += 1
    print(n * x - y)
    return

if __name__ == '__main__':
    main()