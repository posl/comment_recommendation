def get_median(l):
    l = sorted(l)
    length = len(l)
    if length % 2 == 0:
        return int((l[int(length/2)] + l[int(length/2)-1])/2)
    else:
        return l[int((length-1)/2)]

if __name__ == '__main__':
    get_median()