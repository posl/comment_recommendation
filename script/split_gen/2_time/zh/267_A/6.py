def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t, x, a = map(int, input().split())
        snuke.append([t, x, a])
    snuke.sort(key=lambda x: x[0])
    snuke.sort(key=lambda x: x[1])
    snuke = [[0, 0, 0]] + snuke
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], dp[i])
        for j in range(i - 1, -1, -1):
            if snuke[i][1] - snuke[j][1] >= snuke[i][0] - snuke[j][0]:
                dp[i] = max(dp[i], dp[j] + snuke[i][2])
                break
    print(dp[n])
