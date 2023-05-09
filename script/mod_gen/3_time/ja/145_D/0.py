def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if X < N or Y < N:
        print(0)
        return
    print(comb(2 * N, N, 10 ** 9 + 7))

if __name__ == '__main__':
    main()