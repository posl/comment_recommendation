def problems241_a():
    #读取输入
    a = [int(x) for x in input().split()]
    #初始化
    #k为屏幕上显示的数字
    k = 0
    #循环
    for i in range(3):
        k = a[k]
    #输出
    print(k)

if __name__ == '__main__':
    problems241_a()