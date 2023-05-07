def main():
    N, X = map(int, input().split())
    print(chr(65 + (X - 1) % N))

if __name__ == '__main__':
    main()