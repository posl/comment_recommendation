def main():
    a, b = map(int, input().split())
    print(max(a + b - 1, a + a - 1, b + b - 1))

if __name__ == '__main__':
    main()