def main():
    a, b, x = map(int, input().split())
    if x >= a**2 * b / 2:
        print(90 - math.degrees(math.atan(2 * (a**2 * b - x) / a**3)))
    else:
        print(math.degrees(math.atan(a * b**2 / 2 / x)))

if __name__ == '__main__':
    main()