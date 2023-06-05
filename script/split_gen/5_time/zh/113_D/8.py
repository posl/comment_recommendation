def amidakuji(h, w, k):
    #h:垂直线的数量
    #w:水平线的数量
    #k:起始垂直线的位置
    #返回满足条件的羊皮卷的数量
    if h == 1:
        if k == 1:
            return 1
        elif k == w:
            return 1
        else:
            return 0
    elif k == 1:
        return amidakuji(h-1, w, k+1)
    elif k == w:
        return amidakuji(h-1, w, k-1)
    else:
        return amidakuji(h-1, w, k-1) + amidakuji(h-1, w, k+1)
