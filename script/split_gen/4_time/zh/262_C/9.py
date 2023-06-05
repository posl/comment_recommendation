def solve():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))
    # 计算答案
    ans = 0
    for i in range(N):
        if A[i] <= i + 1:
            continue
        for j in range(i + 1, N):
            if A[j] < A[i]:
                ans += 1
    print(ans)
