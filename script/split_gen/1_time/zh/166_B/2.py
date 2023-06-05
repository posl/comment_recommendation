def main():
    # 读入数据
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        d = int(input())
        A.append(list(map(int, input().split())))
    # 算法
    # 1. 初始化
    snuke = [0] * N
    # 2. 遍历
    for i in range(K):
        for j in range(len(A[i])):
            snuke[A[i][j] - 1] += 1
    # 3. 输出
    print(snuke.count(0))
