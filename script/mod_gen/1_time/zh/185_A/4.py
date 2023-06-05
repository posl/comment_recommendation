def main():
    #读取输入
    a = input()
    #print(a)
    #将输入转换成整数数组
    a = list(map(int, a.split()))
    #print(a)
    #计算最小的数值
    min = a[0]
    for i in range(1, len(a)):
        if min > a[i]:
            min = a[i]
    #print(min)
    #计算最大的数值
    max = a[0]
    for i in range(1, len(a)):
        if max < a[i]:
            max = a[i]
    #print(max)
    #计算最大的数值出现的次数
    maxCount = 0
    for i in range(0, len(a)):
        if max == a[i]:
            maxCount += 1
    #print(maxCount)
    #计算最大的数值出现的次数
    minCount = 0
    for i in range(0, len(a)):
        if min == a[i]:
            minCount += 1
    #print(minCount)
    #计算最大的数值出现的次数
    print(maxCount * minCount)

if __name__ == '__main__':
    main()