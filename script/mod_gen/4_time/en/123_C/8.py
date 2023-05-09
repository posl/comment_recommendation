def calc_min_time(n, a, b, c, d, e):
    # n people
    # a train
    # b bus
    # c taxi
    # d airplane
    # e ship
    return int(5 + (n-1)//min(a,b,c,d,e))

if __name__ == '__main__':
    calc_min_time()