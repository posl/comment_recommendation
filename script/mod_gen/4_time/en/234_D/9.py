def find_kth_greatest_value(P, K):
    P = sorted(P)
    return P[-K]

if __name__ == '__main__':
    find_kth_greatest_value()