def calc_follow(a,b):
    if b <= 2 * a + 100:
        return 2 * a + 100 - b
    else:
        return 0

if __name__ == '__main__':
    calc_follow()