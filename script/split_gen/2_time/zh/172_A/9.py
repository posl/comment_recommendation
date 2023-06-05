def main():
    # 读取输入
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    BC = [input().split() for i in range(Q)]
    # 处理
    # 用字典保存每个数出现的次数
    d = dict()
    for i in A:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    # 计算初始和
    sum = 0
    for i in d:
        sum += i * d[i]
    # 每次操作
    for i in range(Q):
        b = int(BC[i][0])
        c = int(BC[i][1])
        # 更新字典
        if b in d:
            d[c] = d[c] + d[b]
            sum += (c - b) * d[b]
            del d[b]
        # 输出
        print(sum)
