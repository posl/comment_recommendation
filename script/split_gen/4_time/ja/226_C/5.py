def main():
    n = int(input())
    tka = []
    for i in range(n):
        tka.append(list(map(int, input().split())))
    tka = tka[::-1]
    for i in range(n):
        if tka[i][1] == 0:
            tka[i][1] = 1
    dp = [0] * (n+1)
    for i in range(n):
        dp[tka[i][2]] = max(dp[tka[i][2]], dp[i+1] + tka[i][0] * tka[i][1])
        if tka[i][2] > 1:
            for j in range(1, tka[i][2]):
                dp[j] = max(dp[j], dp[i+1])
    print(max(dp))
