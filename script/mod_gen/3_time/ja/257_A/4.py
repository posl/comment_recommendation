def main():
    N, X = map(int, input().split())
    print(chr(X % 26 + 64))

if __name__ == '__main__':
    main()