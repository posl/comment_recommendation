def main():
    N = int(input())
    S = input()
    for s in S:
        print(chr((ord(s) - ord('A') + N) % 26 + ord('A')), end='')
    print()

if __name__ == '__main__':
    main()