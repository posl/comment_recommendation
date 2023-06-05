def main():
    x, y = map(int, input().split())
    print((x + 1) % 3 if x == y else 3 - x - y)

if __name__ == '__main__':
    main()