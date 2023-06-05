def get_median(ary):
    ary.sort()
    if len(ary)%2 == 0:
        return ary[len(ary)//2]
    else:
        return ary[len(ary)//2+1]

if __name__ == '__main__':
    get_median()