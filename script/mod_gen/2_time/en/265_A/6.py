def min_price(x, y, n):
    if n % 3 == 0:
        return n // 3 * y
    elif n % 3 == 1:
        return (n // 3) * y + x
    else:
        return (n // 3 + 1) * y

if __name__ == '__main__':
    min_price()