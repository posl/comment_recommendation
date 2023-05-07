def main():
    N, W = map(int, input().split())
    cheese = []
    for _ in range(N):
        A, B = map(int, input().split())
        cheese.append([A, B])
    cheese.sort(key=lambda x: x[0])
    maxA = cheese[-1][0]
    dp = [0] * (maxA * 1000 + 1)
    for A, B in cheese:
        for i in range(maxA * 1000, A - 1, -1):
            dp[i] = max(dp[i], dp[i - A] + B)
    ans = 0
    for i in range(maxA * 1000 + 1):
        if dp[i] >= W:
            ans = i
            break
    print(ans)
main()

if __name__ == '__main__':
    main()