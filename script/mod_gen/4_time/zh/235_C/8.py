def  binary_search(a, x, k):
    '''
    二分查找
    :param a: 数组
    :param x: 查找的数
    :param k: 第几次出现
    :return: 第k次出现的位置
    '''
    # print(a, x, k)
    if k == 1:
        for i in range(len(a)):
            if a[i] == x:
                return i
        return -1
    elif k == 2:
        for i in range(len(a)):
            if a[i] == x:
                k -= 1
            if k == 1:
                return i
        return -1
    else:
        if x in a:
            return a.index(x)
        else:
            return -1

if __name__ == '__main__':
    ()