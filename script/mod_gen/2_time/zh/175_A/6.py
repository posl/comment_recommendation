def max_rainy_days(s):
    if s == 'RRR':
        return 3
    elif s == 'RRS' or s == 'SRR':
        return 2
    elif s == 'SSS':
        return 0
    else:
        return 1

if __name__ == '__main__':
    max_rainy_days()