def print_page(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        if n % 2 == 0:
            return n / 2
        else:
            return n / 2 + 1

if __name__ == '__main__':
    print_page()