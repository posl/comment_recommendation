def calc_price(head, a, x, y):
    if head <= a:
        return head * x
    else:
        return a * x + (head - a) * y

if __name__ == '__main__':
    calc_price()