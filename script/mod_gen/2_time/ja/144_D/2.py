def main():
    a, b, x = map(int, input().split())
    if a * a * b / 2 > x:
        print(math.degrees(math.atan(2 * (a * a * b - x) / (a * a * a))))
    else:
        print(math.degrees(math.atan((a * b * b) / (2 * (a * a * b - x)))))

if __name__ == '__main__':
    main()