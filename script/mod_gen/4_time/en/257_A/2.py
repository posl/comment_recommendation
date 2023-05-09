def main():
    N, X = map(int, input().split())
    print(chr(X - 1 + ord('A')))

if __name__ == '__main__':
    main()