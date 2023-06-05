def main():
    p = int(input())
    coins = [1]
    for i in range(2, 11):
        coins.append(coins[-1] * i)
    count = 0
    for i in range(9, -1, -1):
        count += p // coins[i]
        p %= coins[i]
    print(count)
