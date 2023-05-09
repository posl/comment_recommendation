def main():
    N = int(input())
    trampolines = []
    for _ in range(N):
        x, y, p = map(int, input().split())
        trampolines.append((x, y, p))
    trampolines.sort(key=lambda x: x[2], reverse=True)
    dp = [0] * N
    for i in range(N):
        for j in range(i):
            x1, y1, p1 = trampolines[i]
            x2, y2, p2 = trampolines[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            if p1 * dp[j] >= dist:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp) + 1)
