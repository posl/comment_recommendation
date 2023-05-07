def main():
    N, X, Y = map(int, input().split())
    for k in range(1, N):
        ans = 0
        for i in range(1, N + 1):
            for j in range(i + 1, N + 1):
                if abs(i - j) == k:
                    ans += 1
                elif abs(i - X) + 1 + abs(Y - j) == k:
                    ans += 1
                elif abs(i - Y) + 1 + abs(X - j) == k:
                    ans += 1
        print(ans)

if __name__ == '__main__':
    main()