def red_jewel_to_blue_jewel(n, x, y):
    if n == 1:
        return 0
    elif n == 2:
        return x + y
    else:
        return red_jewel_to_blue_jewel(n-1, x, y) + x + red_jewel_to_blue_jewel(n-1, x, y) + y

if __name__ == '__main__':
    red_jewel_to_blue_jewel()