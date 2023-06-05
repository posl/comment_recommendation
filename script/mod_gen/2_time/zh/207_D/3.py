def main():
    # 读入数据
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    
    # 计算相交的区间
    count = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if (data[i][1] <= data[j][1] and data[j][1] <= data[i][2]) or \
                (data[j][1] <= data[i][1] and data[i][1] <= data[j][2]):
                count += 1
    
    # 输出结果
    print(count)

if __name__ == '__main__':
    main()