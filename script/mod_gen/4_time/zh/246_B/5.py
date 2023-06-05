def main():
    a, b = map(int, input().split())
    x = a * 1.0 / (a * a + b * b) ** 0.5
    y = b * 1.0 / (a * a + b * b) ** 0.5
    print(x, y)

if __name__ == '__main__':
    main()