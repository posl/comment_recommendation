def main():
    a, b, n = map(int, input().split())
    if n >= b:
        x = b - 1
    else:
        x = n
    print((a * x) // b - a * (x // b))

if __name__ == '__main__':
    main()