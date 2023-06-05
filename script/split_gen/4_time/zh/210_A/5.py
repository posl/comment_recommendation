def calc_price(head, a, x, y):
    if head <= a:
        return head * x
    else:
        return a * x + (head - a) * y
