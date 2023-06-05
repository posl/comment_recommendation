def getMinNum(a):
    # a.sort()
    # print(a)
    # for i in range(0,len(a)):
    #     if a[i] != i:
    #         return i
    # return len(a)
    b = [0]*len(a)
    for i in range(0,len(a)):
        if a[i] < len(a):
            b[a[i]] = 1
    for i in range(0,len(b)):
        if b[i] == 0:
            return i
    return len(a)

if __name__ == '__main__':
    getMinNum()