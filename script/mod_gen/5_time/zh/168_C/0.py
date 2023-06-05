def main():
    a, b, h, m = map(int, input().split())
    x = a * (h * 60 + m) / 720
    y = b * m / 60
    print((x ** 2 + y ** 2) ** 0.5)

if __name__ == '__main__':
    main()