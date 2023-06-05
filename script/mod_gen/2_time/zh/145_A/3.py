def main():
    a, b, x = map(int, input().split())
    if x >= a * a * b / 2:
        print(90 - (90 - 2 * (b / a) * (b - x / a / a)) * 180 / 3.141592653589793238)
    else:
        print((90 - 2 * x / a / b / b) * 180 / 3.141592653589793238)

if __name__ == '__main__':
    main()