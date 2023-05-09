def main():
    N, X = map(int, input().split())
    if X <= N:
        print(chr(64 + X))
    else:
        print(chr(64 + ((X % N) + (N if (X % N) == 0 else 0))))

if __name__ == '__main__':
    main()