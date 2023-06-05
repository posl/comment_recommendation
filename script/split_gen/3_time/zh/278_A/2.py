def main():
    # 读取输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 执行k次操作
    for i in range(k):
        # 删除a的初始元素，并在a的尾部附加一个0
        del a[0]
        a.append(0)
    # 输出结果
    print(*a)
