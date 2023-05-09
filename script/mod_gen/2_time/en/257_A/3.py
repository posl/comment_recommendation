def main():
    N, X = map(int, input().split())
    print(chr(ord('A') + (X - 1) // N))

if __name__ == '__main__':
    main()