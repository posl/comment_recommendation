def main():
    a, b, x = map(int, input().split())
    if a * a * b / 2 >= x:
        print(90 - math.degrees(math.atan(2 * x / (a * a * b))))
    else:
        print(math.degrees(math.atan(2 * (a * a * b - x) / (a * a * a))))

if __name__ == '__main__':
    main()