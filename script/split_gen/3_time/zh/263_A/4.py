def main():
    #读取输入
    a,b,c,d,e = map(int,input().split())
    #定义一个列表，存放5张牌
    list1 = [a,b,c,d,e]
    #定义一个字典，存放每张牌出现的次数
    dict1 = {}
    #遍历列表，统计每张牌出现的次数
    for i in list1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    #如果字典中有三个key，且每个key对应的value都为3，则满足条件
    if len(dict1) == 3 and max(dict1.values()) == 3 and min(dict1.values()) == 2:
        print("Yes")
    else:
        print("No")
