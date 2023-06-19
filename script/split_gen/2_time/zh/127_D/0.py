def main():
    # 读入数据
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    # 从大到小排序
    A.sort(reverse=True)
    BC.sort(key=lambda x: x[1], reverse=True)
    # 用于替换的数的索引
    i = 0
    # 用于替换的数的个数
    cnt = 0
    # 替换
    for b, c in BC:
        # 替换的数的索引
        while i < N and A[i] > c and cnt < b:
            A[i] = c
            i += 1
            cnt += 1
    # 输出
    print(sum(A))
