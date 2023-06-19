def main():
    # 读取输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort() # 排序
    # print(n, k, a)
    # 统计每个部门的人数
    count = 1
    num = 0
    for i in range(1, n):
        if a[i] == a[i-1]:
            count += 1
        else:
            num += count // k
            count = 1
    num += count // k
    print(num)
