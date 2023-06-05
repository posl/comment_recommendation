def main():
    # 读取数据
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    # 生成所有可能的质量
    B = set()
    for i in range(N):
        for j in range(i, N):
            for k in range(j, N):
                B.add(A[i] + A[j] + A[k])
    # 计算答案
    ans = 0
    for b in B:
        if b <= W:
            ans += 1
    print(ans)
