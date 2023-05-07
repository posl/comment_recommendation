def get_price(A, B):
    for price in range(1, 1001):
        if int(price * 0.08) == A and int(price * 0.1) == B:
            return price
    return -1

if __name__ == '__main__':
    get_price()