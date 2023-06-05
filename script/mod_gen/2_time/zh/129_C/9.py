def get_min_diff(l):
    l.sort()
    T = sum(l)/2
    S1 = 0
    S2 = 0
    for i in range(len(l)):
        if S1 + l[i] <= T:
            S1 += l[i]
        else:
            S2 += l[i]
    return abs(S1 - S2)

if __name__ == '__main__':
    get_min_diff()