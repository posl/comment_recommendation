def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    n = (X + Y) // 3
    if X > n or Y > n:
        print(0)
        return
    print(comb(n, X, 10**9 + 7))

if __name__ == '__main__':
    main()