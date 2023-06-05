def main():
    '''主函数'''
    #输入
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
    #计算
    #1.计算出所有的坐标
    #2.计算出所有的坐标的差值
    #3.计算出所有的坐标的差值的最大公约数
    #4.计算出所有的坐标的差值的最大公约数的最大值
    #5.最大值+1
    #1.计算出所有的坐标
    x_y = []
    for i in range(n):
        for j in range(i+1, n):
            x_y.append([x[i]-x[j], y[i]-y[j]])
            x_y.append([x[j]-x[i], y[j]-y[i]])
    #2.计算出所有的坐标的差值
    xy = []
    for i in range(len(x_y)):
        xy.append(x_y[i][0])
        xy.append(x_y[i][1])
    #3.计算出所有的坐标的差值的最大公约数
    xy_gcd = xy[0]
    for i in range(len(xy)-1):
        xy_gcd = gcd(xy_gcd, xy[i+1])
    #4.计算出所有的坐标的差值的最大公约数的最大值
    xy_gcd_max = xy_gcd
    for i in range(len(xy)):
        xy_gcd_max = max(xy_gcd_max, xy[i])
    #5.最大值+1
    print(xy_gcd_max//xy_gcd+1)
