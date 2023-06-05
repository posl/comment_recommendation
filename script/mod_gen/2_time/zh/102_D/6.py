def main():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))
    # 累计和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 二分查找
    result = 10**9
    for i in range(2, N - 1):
        for j in range(i + 1, N):
            # P = S[i]
            # Q = S[j] - S[i]
            # R = S[N] - S[j]
            # S = S[N] - S[i]
            # result = min(result, max(P, Q, R, S) - min(P, Q, R, S))
            # 优化
            P = S[i]
            Q = S[j] - S[i]
            R = S[N] - S[j]
            S = S[N] - S[i]
            result = min(result, max(P, Q, R, S) - min(P, Q, R, S))
            # 二分查找
            # 1. 二分查找的对象是什么？是最大值和最小值的绝对差
            # 2. 二分查找的范围是什么？是最大值和最小值的绝对差的范围
            # 3. 二分查找的条件是什么？是最大值和最小值的绝对差是否大于等于当前值
            # 4. 二分查找的结果是什么？是最大值和最小值的绝对差的最小值
            # 5. 二分查找的返回值是什么？是最大值和最小值的绝对差的最小值
            # 6. 二分查找的实现是什么？是二分查找的实现
            # 7. 二分查找的时间复杂度是什么？是O(log N)
            # 8. 二分查找的空

if __name__ == '__main__':
    main()