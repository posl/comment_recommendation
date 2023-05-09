def main():
    n = int(input())
    s = input()
    for c in s:
        print(chr((ord(c) - ord('A') + n) % 26 + ord('A')), end='')
    print()

if __name__ == '__main__':
    main()