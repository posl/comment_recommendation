def hex(n):
    if n < 10:
        return n
    elif n == 10:
        return 'A'
    elif n == 11:
        return 'B'
    elif n == 12:
        return 'C'
    elif n == 13:
        return 'D'
    elif n == 14:
        return 'E'
    elif n == 15:
        return 'F'
    else:
        return None

if __name__ == '__main__':
    hex()