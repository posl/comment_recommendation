def cut_rod(n):
    if n==0:
        return 1
    if n<0:
        return 0
    return sum([cut_rod(n-i) for i in range(1,12+1)])

if __name__ == '__main__':
    cut_rod()