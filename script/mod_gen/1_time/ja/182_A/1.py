def main():
    a, b = map(int, input().split())
    if 2 * a + 100 < b:
        print(0)
    else:
        print(2 * a + 100 - b)

if __name__ == '__main__':
    main()