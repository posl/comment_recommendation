def main():
    p = list(map(int, input().split()))
    for i in range(26):
        print(chr(ord('a') + p[i] - 1), end='')
    print()

if __name__ == '__main__':
    main()