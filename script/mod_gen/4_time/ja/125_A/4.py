def calc_biscuits(a, b, t):
    num = 0
    for i in range(1, t+1):
        if i % a == 0:
            num += b
    return num

if __name__ == '__main__':
    calc_biscuits()