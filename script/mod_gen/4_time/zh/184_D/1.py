def main():
    a, b, c = map(int, input().split())
    print((a * (a + b + c) - a * a) / (a + b + c - a))

if __name__ == '__main__':
    main()