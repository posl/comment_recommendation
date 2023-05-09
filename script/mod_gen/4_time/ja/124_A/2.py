def main():
    a, b = map(int, input().split())
    if a == b:
        print(2 * a)
    else:
        print(max(2 * a - 1, 2 * b - 1, a + b))

if __name__ == '__main__':
    main()