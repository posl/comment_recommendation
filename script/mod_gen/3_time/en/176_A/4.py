def main():
    N, X, T = map(int, input().split())
    ans = 0
    ans = N // X * T
    if N % X != 0:
        ans += T
    print(ans)

if __name__ == '__main__':
    main()