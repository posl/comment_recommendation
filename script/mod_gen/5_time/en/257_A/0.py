def main():
    N, X = map(int, input().split())
    print(chr(ord('A') + (X - 1) % 26))

if __name__ == '__main__':
    main()