def main():
    A, B, X = map(int, input().split())
    N = 0
    while True:
        if A * N + B * len(str(N)) > X:
            break
        N += 1
    print(N - 1)

if __name__ == '__main__':
    main()