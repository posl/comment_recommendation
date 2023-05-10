def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t,x,a = map(int,input().split())
        snuke.append((t,x,a))
    snuke.append((0,0,0))
    snuke.append((10**5,0,0))
    snuke.sort()
    dp = [0]*(n+2)
    for i in range(1,n+2):
        dp[i] = max(dp[i-1],dp[i])
        if snuke[i-1][1] == snuke[i][1]:
            dp[i] = max(dp[i],dp[i-1]+snuke[i][2])
        else:
            dp[i] = max(dp[i],dp[i-1]+snuke[i][2]-abs(snuke[i][1]-snuke[i-1][1]))
    print(dp[n+1])
