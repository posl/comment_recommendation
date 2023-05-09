def main():
    x, y = map(int, input().split())
    print((y - x % y) % y)

if __name__ == '__main__':
    main()