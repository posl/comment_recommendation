def print_order_string(a, b, k):
    if a == 0:
        return 'b' * b
    elif b == 0:
        return 'a' * a
    elif a == 1 and b == 1:
        if k == 1:
            return 'ab'
        else:
            return 'ba'
    else:
        if k <= combination(a+b-1, a-1):
            return 'a' + print_order_string(a-1, b, k)
        else:
            return 'b' + print_order_string(a, b-1, k - combination(a+b-1, a-1))
