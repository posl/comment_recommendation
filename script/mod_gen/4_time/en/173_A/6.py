def buy_product():
    n = int(input())
    return (1000 - (n % 1000)) % 1000
print(buy_product())
