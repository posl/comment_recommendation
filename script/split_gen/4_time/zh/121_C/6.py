def shop_list():
    #初始化
    n = 0
    m = 0
    shop_list = []
    #输入
    n, m = map(int, input().split())
    for i in range(n):
        shop_list.append(list(map(int, input().split())))
    #排序
    shop_list.sort(key=lambda x: x[0])
    #计算
    count = 0
    money = 0
    for i in range(n):
        if count + shop_list[i][1] < m:
            count += shop_list[i][1]
            money += shop_list[i][0] * shop_list[i][1]
        else:
            money += shop_list[i][0] * (m - count)
            break
    #输出
    print(money)
shop_list()
