def is_payable(n, x, a, b):
    if n == 1:
        if x % a[0] == 0 and x / a[0] <= b[0]:
            return True
        else:
            return False
    else:
        for i in range(b[0] + 1):
            if is_payable(n - 1, x - a[0] * i, a[1:], b[1:]):
                return True
        return False

if __name__ == '__main__':
    is_payable()