def double_sided_printing(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n // 2 + 1

if __name__ == '__main__':
    double_sided_printing()