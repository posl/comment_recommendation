def buy_apple(x, y, n):
    if n % 3 == 0:
        return y * (n // 3)
    else:
        return y * (n // 3) + x * (n % 3)

if __name__ == '__main__':
    buy_apple()