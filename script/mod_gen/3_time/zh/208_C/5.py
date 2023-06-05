def main():
    # 读取输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 排序
    a.sort()
    # 计算每个人的糖果
    candy = k // n
    # 余下的糖果
    remain = k % n
    # 计算每个人的糖果
    for i in range(n):
        if a[i] < remain:
            print(candy + 1)
        else:
            print(candy)

if __name__ == '__main__':
    main()