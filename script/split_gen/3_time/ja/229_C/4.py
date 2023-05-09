def main():
    N, W = map(int, input().split())
    cheese = []
    for _ in range(N):
        a, b = map(int, input().split())
        cheese.append([a, b])
    cheese.sort(reverse=True)
    #print(cheese)
    dp = [0] * (W+1)
    for i in range(N):
        for j in range(W, cheese[i][1]-1, -1):
            dp[j] = max(dp[j], dp[j-cheese[i][1]] + cheese[i][0])
    print(dp[W])
