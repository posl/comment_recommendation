def main():
    a, b, n = map(int, input().split())
    if b - 1 <= n:
        print((a * (b - 1)) // b)
    else:
        print((a * n) // b)

if __name__ == '__main__':
    main()