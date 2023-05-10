def main():
    a, b = map(int, input().split())
    x = b - a
    y = (x * (x + 1)) // 2
    print(y - b)

if __name__ == '__main__':
    main()