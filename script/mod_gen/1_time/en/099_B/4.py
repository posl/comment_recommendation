def main():
    a, b = map(int, input().split())
    x = 0
    x = (b * (b + 1)) // 2 - (a * (a - 1)) // 2
    print(x - (b - a))

if __name__ == '__main__':
    main()