def main():
    """
    #思路：
    #1.先读取输入数据，存入列表中
    #2.遍历列表，找出每张数字牌的位置
    #3.打印每张数字牌的位置
    """
    #1.先读取输入数据，存入列表中
    h, w, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    #2.遍历列表，找出每张数字牌的位置
    #初始化一个列表，用于存储每张数字牌的位置
    c = [0 for i in range(n)]
    d = [0 for i in range(n)]
    #遍历列表，找出每张数字牌的位置
    for i in range(n):
        #如果当前行没有数字牌
        if a.count(a[i]) == 1:
            #将当前行的所有牌拿掉
            for j in range(n):
                if a[j] == a[i]:
                    a[j] = 0
            #将剩下的牌往上移，填补这个空缺
            for j in range(n):
                if a[j] > a[i]:
                    a[j] -= 1
        #如果当前列没有数字牌
        if b.count(b[i]) == 1:
            #将当前列的所有牌拿掉
            for j in range(n):
                if b[j] == b[i]:
                    b[j] = 0
            #将剩下的牌往左移，以填补这个缺口
            for j in range(n):
                if b[j] > b[i]:
                    b[j] -= 1
        #找出每张数字牌的位置
        c[i] = a[i]
        d[i] = b[i]
    #3.打印每张数字牌的位置
    for i in range(n):
        print(c[i], d[i])

if __name__ == '__main__':
    main()