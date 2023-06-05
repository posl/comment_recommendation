def main():
    # 读取输入
    n = int(input())
    stores = []
    for i in range(n):
        store = list(map(int, input().split()))
        stores.append(store)
    # print(stores)
    # 计算结果
    result = -1
    for i in range(n):
        if stores[i][2] > 0:
            if result == -1:
                result = stores[i][1]
            elif result > stores[i][1]:
                result = stores[i][1]
    # 输出结果
    print(result)

if __name__ == '__main__':
    main()