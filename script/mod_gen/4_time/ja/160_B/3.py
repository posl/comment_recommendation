def exchange(x):
    coins = [500, 100, 50, 10, 5, 1]
    count = 0
    for coin in coins:
        count += x // coin
        x %= coin
    return count
print(exchange(int(input())) * 1000)

if __name__ == '__main__':
    exchange()