def main():
    a, b, x = map(int, input().split())
    if x < a**2 * b / 2:
        h = (2 * x) / (a * b)
        print(math.degrees(math.atan(b / h)))
    else:
        h = (2 * (a**2 * b - x)) / (a * b)
        print(math.degrees(math.atan(h / a)))

if __name__ == '__main__':
    main()