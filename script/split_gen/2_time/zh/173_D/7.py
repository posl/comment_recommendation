def solve():
    N = int(input())
    A = list(map(int, input().split()))
    # 从1开始，因为第一个人的舒适度为0
    B = [0] * (N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    # 原问题转换为：从第i个人开始，逆时针走，一直到第j个人结束，这个区间的最小值是多少
    # 用单调栈来解决
    # 从左往右扫描，栈里面存储的是递增的序列，如果遇到比栈顶小的数，就把栈顶弹出来，直到栈顶比当前数大，然后把当前数压入栈顶
    # 那么每个数进栈一次，出栈一次，所以算法复杂度是O(n)
    stack = []
    ans = 0
    for i in range(N+1):
        # 如果当前数比栈顶小，就把栈顶弹出来
        while len(stack) > 0 and A[stack[-1]] > A[i]:
            j = stack.pop()
            # 栈顶弹出来的时候，栈顶是第j个人，栈顶的下一个是第i个人
            # 那么，第j个人到第i个人之间的最小值是A[j]
            # 第j个人到第i个人之间的舒适度是A[j] * (B[i] - B[j])
            ans = max(ans, A[j] * (B[i] - B[j]))
        # 把当前数压入栈顶
        stack.append(i)
    print(ans)
solve()
