def main():
    X, Y = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    if (X + Y) % 3 != 0:
        print(0)
        return
    N = (X + Y) // 3
    if N < max(X, Y):
        print(0)
        return
    ans = comb(N, X, MOD)
    print(ans)

if __name__ == '__main__':
    main()