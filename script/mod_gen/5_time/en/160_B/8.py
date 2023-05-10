def coin_exchange():
    x = int(input())
    n = x // 500
    m = (x % 500) // 5
    print(n * 1000 + m * 5)

if __name__ == '__main__':
    coin_exchange()