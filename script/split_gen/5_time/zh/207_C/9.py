def main():
    #读取输入数据
    n = int(input())
    data = []
    for i in range(n):
        data.append([int(x) for x in input().split()])
    #统计交叉点
    count = 0
    for i in range(n-1):
        for j in range(i+1,n):
            #判断是否相交
            if data[i][1]<=data[j][1] and data[j][1]<=data[i][2] or data[j][1]<=data[i][1] and data[i][1]<=data[j][2]:
                count += 1
    #输出结果
    print(count)
main()
