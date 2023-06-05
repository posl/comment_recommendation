def water_the_flowers(N, h):
    #不要忘记最后一个花朵
    h.append(0)
    #初始化
    l = 0
    r = 0
    #花朵高度
    hight = 0
    #浇水次数
    count = 0
    #当r小于N时，循环
    while r < N:
        #如果花朵高度等于0，l和r都加1
        if hight == 0:
            l += 1
            r += 1
            #花朵高度加1
            hight += 1
        #如果花朵高度不等于0，r加1
        else:
            r += 1
            #如果花朵高度小于r-l+1，花朵高度加1
            if hight < r - l + 1:
                hight += 1
            #如果花朵高度大于r-l+1，花朵高度减1
            elif hight > r - l + 1:
                hight -= 1
            #如果花朵高度等于r-l+1，花朵高度不变
            else:
                pass
        #浇水次数加1
        count += 1
    return count
