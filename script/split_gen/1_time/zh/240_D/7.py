def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))
    # 各个数字的数量
    count = {}
    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    # 每个数字的最大长度
    length = {}
    for i in count:
        length[i] = 1
    # 从小到大遍历
    for i in range(2, max(a) + 1):
        if i in count:
            # 如果有i的数字
            # 从小到大遍历i的倍数，更新最大长度
            for j in range(2 * i, max(a) + 1, i):
                if j in length and length[j] < length[i] + 1:
                    length[j] = length[i] + 1
    # 输出
    for i in a:
        print(n - length[i] + 1)
