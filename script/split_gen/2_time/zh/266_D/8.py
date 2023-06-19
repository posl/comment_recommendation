def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t,x,a = map(int,input().split())
        snuke.append((t,x,a))
    snuke.sort()
    dp = [0] * 5
    for t,x,a in snuke:
        dp[x] = max(dp[x],dp[x-1]+a)
    print(max(dp))
