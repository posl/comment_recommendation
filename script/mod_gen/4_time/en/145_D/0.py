def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X > N or Y > N:
        print(0)
        return
    N -= 1
    X -= 1
    Y -= 1
    print(comb(N, X, 10**9 + 7))

if __name__ == '__main__':
    main()