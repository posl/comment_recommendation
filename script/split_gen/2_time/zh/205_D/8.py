def main():
    # 读入数据
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    # 处理数据
    # 1. 计算所有正整数
    # 2. 对所有正整数排序
    # 3. 计算第K个最小的整数
    # 4. 输出结果
    # 1. 计算所有正整数
    all_int = []
    for i in range(n):
        if i == 0:
            all_int += list(range(1, a[0]))
        else:
            all_int += list(range(a[i - 1] + 1, a[i]))
    all_int += list(range(a[n - 1] + 1, 10 ** 18 + 1))
    # 2. 对所有正整数排序
    all_int.sort()
    # 3. 计算第K个最小的整数
    for i in range(q):
        print(all_int[k[i] - 1])
