def get_coin_number(n):
    coin_number = 0
    for i in range(10, 0, -1):
        if n >= i:
            coin_number += n // i
            n = n % i
    return coin_number

if __name__ == '__main__':
    get_coin_number()