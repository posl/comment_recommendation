def main():
    P = int(input())
    coins = [1]
    for i in range(2, 11):
        coins.append(coins[i-2]*i)
    count = 0
    for i in range(9, -1, -1):
        count += P // coins[i]
        P = P % coins[i]
    print(count)
