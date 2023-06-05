def main():
    a, b, c, x = map(int, input().split())
    print(c / (b - a + 1) if a <= x <= b else 0)

if __name__ == '__main__':
    main()