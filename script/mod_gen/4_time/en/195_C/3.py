def count_comma(n):
    if n < 1000:
        return 0
    elif n < 1000000:
        return n - 999
    elif n < 1000000000:
        return 2 * (n - 999999) + 999000
    elif n < 1000000000000:
        return 3 * (n - 999999999) + 2 * 999000000 + 999000
    elif n < 1000000000000000:
        return 4 * (n - 999999999999) + 3 * 999000000000 + 2 * 999000000 + 999000
    else:
        return 5 * (n - 999999999999999) + 4 * 999000000000000 + 3 * 999000000000 + 2 * 999000000 + 999000
print(count_comma(int(input())))

if __name__ == '__main__':
    count_comma()