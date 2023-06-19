def is_even_digit(n):
    n = str(n)
    if len(n) % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    is_even_digit()