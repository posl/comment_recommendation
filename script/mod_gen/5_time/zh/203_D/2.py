def get_median(a, b, c, d):
    #print(a, b, c, d)
    tmp = sorted([a, b, c, d])
    return tmp[1]

if __name__ == '__main__':
    get_median()