def main():
    a, b, x = map(int, input().split())
    if x <= a * a * b / 2:
        ans = math.degrees(math.atan((2 * x) / (a * a * b)))
    else:
        ans = math.degrees(math.atan((2 * (a * a * b - x)) / (a * a * a)))
    print(ans)

if __name__ == '__main__':
    main()