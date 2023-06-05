def solve(N, M, A):
    # 从大到小排序
    A.sort(reverse=True)
    # 从大到小排序的累加和
    A_sum = [0 for i in range(N)]
    A_sum[0] = A[0]
    for i in range(1, N):
        A_sum[i] = A_sum[i-1] + A[i]
    # 从大到小排序的累加和的模M
    A_mod = [0 for i in range(N)]
    for i in range(N):
        A_mod[i] = A_sum[i] % M
    # 去掉A_mod中的0
    A_mod = [i for i in A_mod if i != 0]
    # 求和
    ans = sum(A_mod)
    return ans

if __name__ == '__main__':
    solve()