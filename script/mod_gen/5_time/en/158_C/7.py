def calc_price(A, B):
    for i in range(1, 1001):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            return i
    return -1

if __name__ == '__main__':
    calc_price()