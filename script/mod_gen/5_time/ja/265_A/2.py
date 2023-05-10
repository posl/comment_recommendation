def main():
    X, Y, N = map(int, input().split())
    ans = 0
    ans += (N // 3) * min(3 * X, Y)
    ans += (N % 3) * X
    print(ans)

if __name__ == '__main__':
    main()