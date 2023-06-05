def main():
    n = int(input())
    for i in range(0, n):
        print(chr(ord('A') + i), end='')
    print()

if __name__ == '__main__':
    main()