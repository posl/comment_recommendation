def main():
    #读取输入
    n = int(input())
    a = list(map(int, input().split()))
    #计算最大值
    max = 0
    for i in range(n):
        #计算角度
        angle = 360.0 / 2.0 - a[i]
        #如果角度大于180，就用360减去角度
        if(angle > 180):
            angle = 360 - angle
        #如果角度大于max，就更新max
        if(angle > max):
            max = angle
    #打印结果
    print(int(max))

if __name__ == '__main__':
    main()