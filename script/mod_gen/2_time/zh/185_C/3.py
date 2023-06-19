def cut_rod(L):
    if L == 0:
        return 1
    elif L < 0:
        return 0
    else:
        return sum([cut_rod(L-i) for i in range(1,12+1)])

if __name__ == '__main__':
    cut_rod()