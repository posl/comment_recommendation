def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 从小到大排序
    a.sort()
    # 每个人最少拿一个
    k = k - n
    # 每个人拿的个数
    num = k // n
    # 拿不完的人数
    num2 = k % n
    # 拿不完的人的id
    id = a[num2]
    # 拿完的人拿的个数
    num3 = num + 1
    # 拿完的人的id
    id2 = id - 1
    # 输出
    for i in range(n):
        if a[i] <= id:
            print(num3)
        else:
            print(num)

if __name__ == '__main__':
    main()