def main():
    a, b = map(int, input().split())
    if a > b:
        print(a + b - 1)
    else:
        print(a + b)

if __name__ == '__main__':
    main()