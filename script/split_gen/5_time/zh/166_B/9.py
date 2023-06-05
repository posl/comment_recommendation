def main():
    # 读入数据
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))
    # 初始化
    Snukes = [0] * N
    # 计算
    for i in range(K):
        for j in range(d[i]):
            Snukes[A[i][j]-1] += 1
    # 输出
    print(Snukes.count(0))
