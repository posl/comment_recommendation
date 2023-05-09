def main():
    p = int(input())
    coins = [1,2,3,4,5,6,7,8,9,10]
    for i in range(11,10000000):
        coins.append(coins[-1]*i)
    ans = 0
    for i in range(len(coins)-1,-1,-1):
        if p >= coins[i]:
            ans += p // coins[i]
            p = p % coins[i]
    print(ans)
