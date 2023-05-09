def main():
    P = int(input())
    coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    coins.reverse()
    count = 0
    for coin in coins:
        if P >= coin:
            count += P // coin
            P %= coin
    print(count)
