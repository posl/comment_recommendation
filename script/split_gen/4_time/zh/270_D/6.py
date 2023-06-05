def solve():
    # 读入数据
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 贪心法
    ans = 0
    # 从大到小排序
    A.sort(reverse=True)
    # 从大到小遍历
    for i in range(K):
        # 从大到小遍历
        for j in range(A[i]):
            # 如果N为0，跳出循环
            if N == 0:
                break
            # 否则N减1
            N -= 1
            # ans加1
            ans += 1
    # 输出结果
    print(ans)
solve()
