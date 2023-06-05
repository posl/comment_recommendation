def get_median(b):
    b.sort()
    return b[int(len(b)/2)]

if __name__ == '__main__':
    get_median()