def problem175_a(s):
    if s == 'RRR':
        return 3
    elif s == 'RRS' or s == 'SRR':
        return 2
    elif s == 'SSS':
        return 0
    else:
        return 1

if __name__ == '__main__':
    problem175_a()