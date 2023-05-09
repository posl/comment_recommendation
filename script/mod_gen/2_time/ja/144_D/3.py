def main():
    a, b, x = map(int, input().split())
    if a ** 2 * b / 2 >= x:
        print(math.degrees(math.atan(2 * x / a ** 3)))
    else:
        print(math.degrees(math.atan(a ** 2 / (2 * x / a ** 2 - b))))

if __name__ == '__main__':
    main()