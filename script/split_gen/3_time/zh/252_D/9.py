def three_trio():
    # 读取N
    N = int(input())
    # 读取A
    A = list(map(int, input().split(' ')))
    # 三联体数量
    trio = 0
    # A_i
    for i in range(N - 2):
        # A_j
        for j in range(i + 1, N - 1):
            # A_k
            for k in range(j + 1, N):
                if A[i] != A[j] and A[j] != A[k] and A[i] != A[k]:
                    trio += 1
    return trio
print(three_trio())
