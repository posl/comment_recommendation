def main():
    # 读入数据
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 从最后一个石头开始，一直向前，每次减去A[i]个石头
    ans = 0
    for i in range(K-1, -1, -1):
        # 如果剩下的石头比A[i]大，那么就可以减去A[i]个石头
        if N >= A[i]:
            # 剩下的石头减去A[i]个，得到最后剩下的石头数
            N -= A[i]
            # 由于高桥先开始，所以只有当i为偶数时，才可以加上A[i]个石头
            if i % 2 == 0:
                ans += A[i]
        # 如果剩下的石头比A[i]小，那么就可以减去剩下的石头
        else:
            ans += N
            break
    # 输出答案
    print(ans)
