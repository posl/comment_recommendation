def main():
    P = int(input())
    coins = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    count = 0
    for coin in coins:
        count += P // coin
        P %= coin
    print(count)
