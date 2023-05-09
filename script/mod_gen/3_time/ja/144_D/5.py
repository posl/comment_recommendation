def main():
    a, b, x = map(int, input().split())
    if a * a * b / 2 <= x:
        print(180 * math.atan(2 * (a * a * b - x) / (a * a * a)) / math.pi)
    else:
        print(180 * math.atan(a * b * b / (2 * x)) / math.pi)

if __name__ == '__main__':
    main()