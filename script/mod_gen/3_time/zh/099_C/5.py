def get_num(n):
    if n == 1:
        return 1
    elif n == 6:
        return 1
    elif n == 9:
        return 1
    else:
        if n % 9 == 0:
            return int(n / 9)
        elif n % 6 == 0:
            return int(n / 6)
        else:
            return int(n / 9) + int(n % 9 / 6) + int(n % 6)

if __name__ == '__main__':
    get_num()