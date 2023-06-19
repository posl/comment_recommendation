def main():
    # 读取输入
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    # 排序
    X.sort()
    # 计算相邻两个棋子之间的距离
    dist = []
    for i in range(M-1):
        dist.append(X[i+1] - X[i])
    # 排序
    dist.sort()
    # 计算距离之和
    sum_dist = 0
    for i in dist:
        sum_dist += i
    # 输出
    print(sum_dist - (N-1))
