def main():
    n, x = map(int, input().split())
    a = 26 * n
    if x <= a:
        print(chr(ord('A') + ((x-1) % 26)))
    else:
        x -= a
        print(chr(ord('A') + ((x-1) // n)))

if __name__ == '__main__':
    main()