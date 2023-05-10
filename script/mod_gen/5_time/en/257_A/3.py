def main():
    n, x = map(int, input().split())
    print(chr(65 + x // n - 1))

if __name__ == '__main__':
    main()