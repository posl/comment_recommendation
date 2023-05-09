def main():
    a, b, x = map(int, input().split())
    if x > a ** 2 * b / 2:
        h = (a ** 2 * b - x) * 2 / a ** 2
        print(math.degrees(math.atan(b / h)))
    else:
        h = x * 2 / a / b
        print(math.degrees(math.atan(h / a)))

if __name__ == '__main__':
    main()