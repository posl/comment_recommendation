def main():
    a, b, c = map(int, input().split())
    print(c if a >= b + c else a + b - c)

if __name__ == '__main__':
    main()