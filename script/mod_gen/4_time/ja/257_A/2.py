def main():
    n, x = map(int, input().split())
    print(chr(x % 26 + 64))

if __name__ == '__main__':
    main()