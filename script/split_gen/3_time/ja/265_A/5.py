def main():
    x, y, n = map(int, input().split())
    # 1個ずつ買う場合
    min_price = x * n
    # 3個ずつ買う場合
    for i in range(n + 1):
        price = x * i + y * (n - i)
        if price < min_price:
            min_price = price
    print(min_price)
