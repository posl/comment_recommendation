def main():
    a, b, x = map(int, input().split())
    if x < a ** 2 * b / 2:
        print((180 / math.pi) * math.atan(2 * x / (a ** 2)))
    else:
        print((180 / math.pi) * math.atan(2 * (a ** 2 * b - x) / (a ** 3)))

if __name__ == '__main__':
    main()