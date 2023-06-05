def is_even_digit(n):
    if n < 10:
        return False
    else:
        s = str(n)
        return len(s) % 2 == 0

if __name__ == '__main__':
    is_even_digit()