def main():
    N, X = map(int, input().split())
    print(chr(64 + (X - 1) % 26))

if __name__ == '__main__':
    main()