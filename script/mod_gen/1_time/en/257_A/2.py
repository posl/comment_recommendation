def main():
    n, x = map(int, input().split())
    if x <= n:
        print(chr(64 + x))
    else:
        print(chr(64 + x - n))

if __name__ == '__main__':
    main()