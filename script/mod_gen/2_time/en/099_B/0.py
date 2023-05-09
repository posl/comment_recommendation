def main():
    a, b = map(int, input().split())
    print((b * (b + 1) // 2) - (a * (a - 1) // 2) - a)

if __name__ == '__main__':
    main()