def main():
    a, b = map(int, input().split())
    print((b - a - 1) * (b - a) // 2 - a)

if __name__ == '__main__':
    main()