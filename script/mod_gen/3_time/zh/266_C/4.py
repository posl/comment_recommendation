def is_convex(x1, y1, x2, y2, x3, y3, x4, y4):
    #判断是否是凸四边形
    #计算两个向量的叉乘
    def cross_product(x1, y1, x2, y2):
        return x1 * y2 - x2 * y1
    v1 = cross_product(x2-x1, y2-y1, x3-x2, y3-y2)
    v2 = cross_product(x3-x2, y3-y2, x4-x3, y4-y3)
    v3 = cross_product(x4-x3, y4-y3, x1-x4, y1-y4)
    v4 = cross_product(x1-x4, y1-y4, x2-x1, y2-y1)
    if v1 * v2 >= 0 and v2 * v3 >= 0 and v3 * v4 >= 0 and v4 * v1 >= 0:
        return True
    else:
        return False

if __name__ == '__main__':
    is_convex()