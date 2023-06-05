def main():
    # 读取数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 执行k次操作
    for i in range(k):
        # 删除第一个元素
        a.pop(0)
        # 在末尾添加0
        a.append(0)
    # 输出结果
    print(*a)

if __name__ == '__main__':
    main()