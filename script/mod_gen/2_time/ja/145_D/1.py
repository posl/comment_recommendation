def main():
    X, Y = map(int, input().split())
    if X < Y:
        X, Y = Y, X
    if (X + Y) % 3 != 0:
        print(0)
    else:
        n = (X + Y) // 3
        k = X - n
        print(comb(n, k, 10 ** 9 + 7))

if __name__ == '__main__':
    main()