def main():
    # 读入
    n = int(input())
    # 处理
    # 1. 求出所有的平方数，存入列表
    sq_list = []
    for i in range(1, n+1):
        if i*i > n:
            break
        sq_list.append(i*i)
    # 2. 遍历平方数列表，计算满足条件的数对
    count = 0
    for i in sq_list:
        for j in sq_list:
            if i*j <= n:
                count += 1
    # 输出
    print(count)

if __name__ == '__main__':
    main()