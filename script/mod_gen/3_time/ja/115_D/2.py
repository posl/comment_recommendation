def main():
    N, X = map(int, input().split())
    if N == 0:
        print(1 if X > 0 else 0)
        return
    if X == 1:
        print(0)
        return
    if X == 2 ** (N + 3) - 3:
        print(2 ** (N + 2) - 1)
        return
    if X <= 2 ** (N + 2) - 3:
        main()
        return
    if X <= 2 ** (N + 2) - 2:
        print(2 ** (N + 1) - 1)
        return
    main(X - 2 ** (N + 2) + 2)

if __name__ == '__main__':
    main()