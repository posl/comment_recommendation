def main():
    #从标准输入读取
    a,b,c,d,e = map(int,input().split())
    #定义一个字典，key是数字，value是出现的次数
    dict = {
        a:0,
        b:0,
        c:0,
        d:0,
        e:0
    }
    #遍历输入的数字，统计每个数字出现的次数
    for i in [a,b,c,d,e]:
        dict[i] += 1
    #判断是否满足满堂红的条件
    #如果字典中有一个元素出现3次，另一个元素出现2次，则满足条件
    if 3 in dict.values() and 2 in dict.values():
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()