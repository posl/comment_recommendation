def main():
    P = int(input())
    coins = [1]
    for i in range(1,11):
        coins.append(coins[i-1]*(i+1))
    count = 0
    for i in range(10,0,-1):
        count += P//coins[i]
        P = P%coins[i]
    print(count)
