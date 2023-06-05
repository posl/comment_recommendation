def compute(s):
    count = 0
    for i in range(10000):
        istr = str(i).zfill(4)
        if ismatch(istr, s):
            count += 1
    return count

if __name__ == '__main__':
    compute()