def main():
    N, X, Y = map(int, input().split())
    ans = 0
    for i in range(1, N):
        ans += i * (N - i)
    ans *= X
    ans += N * Y
    print(ans)

if __name__ == '__main__':
    main()