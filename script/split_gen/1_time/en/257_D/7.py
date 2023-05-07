def main():
    N = int(input())
    trampolines = []
    for _ in range(N):
        trampolines.append([int(x) for x in input().split()])
    trampolines.sort(key=lambda x: x[2])
    dp = [0] * N
    for i in range(N):
        p, x, y = trampolines[i]
        dp[i] = max(dp[j] for j in range(i) if (x - trampolines[j][1]) ** 2 + (y - trampolines[j][2]) ** 2 <= (p - trampolines[j][0]) ** 2) + 1
    print(max(dp))
