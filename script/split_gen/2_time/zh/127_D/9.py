def main():
    # 读入数据
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for i in range(M)]
    # 按照A_i的大小顺序从大到小排序
    A.sort(reverse=True)
    # 降序排列BC
    BC.sort(key=lambda x: x[1], reverse=True)
    # 从大到小依次选取BC
    j = 0
    for i in range(N):
        if j < M and A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1
    # 输出结果
    print(sum(A))
