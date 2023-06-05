def main():
    #读取数据
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int,input().split())))
    #遍历所有的组合
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if data[i][1] <= data[j][2] and data[i][2] >= data[j][1]:#判断是否相交
                count += 1
    print(count)

if __name__ == '__main__':
    main()