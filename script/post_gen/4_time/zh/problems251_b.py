Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))

    # print(N, W, A)

    # 1. 从小到大排序
    A.sort()
    # print(A)

    # 2. 求和
    sum_A = sum(A)

    # 3. 求最大值
    max_A = max(A)

    # 4. 求最小值
    min_A = min(A)

    # 5. 求平均值
    ave_A = sum_A / N

    # 6. 求中位数
    if N % 2 == 1:
        mid_A = A[N // 2]
    else:
        mid_A = (A[N // 2 - 1] + A[N // 2]) / 2

    # 7. 求众数
    # 众数是指一个数据序列中出现次数最多的数值
    # 众数不一定存在
    # 众数可能不止一个
    # 众数可能不��

=======
Suggestion 2

def solve(n, w, a):
    a.sort()
    dp = [0] * (w + 1)
    for i in range(n):
        for j in range(w + 1):
            if j >= a[i]:
                dp[j] = max(dp[j], dp[j - a[i]] + a[i])
    return dp[w]

=======
Suggestion 3

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    ans = 0
    for i in range(N):
        for j in range(i, N):
            for k in range(j, N):
                if A[i] + A[j] + A[k] <= W:
                    ans += 1
    print(ans)

main()

=======
Suggestion 4

def main():
    n,w = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    #print(a)
    #print(w)
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum > w:
            break
    print(i)

=======
Suggestion 5

def main():
    N,W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        for j in range(i,N):
            for k in range(j,N):
                if A[i] + A[j] + A[k] <= W:
                    count += 1
    print(count)

=======
Suggestion 6

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

=======
Suggestion 7

def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = list(set(a))
    a.sort()
    ans = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            for k in range(j, len(a)):
                if a[i] + a[j] + a[k] <= w:
                    ans += 1
    print(ans)

=======
Suggestion 8

def get_good_int(N,W,A):
    A.sort()
    B = [0]
    for i in range(N):
        for j in range(i,N):
            for k in range(j,N):
                B.append(A[i]+A[j]+A[k])
    B = list(set(B))
    B.sort()
    C = []
    for i in B:
        if i <= W:
            C.append(i)
    return len(C)

=======
Suggestion 9

def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if a[i] + a[j] + a[k] <= w:
                    ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))

    # 重量的范围是1~W，因此我们只需要考虑重量的和W以下的情况
    # 用dp[i]表示重量和为i的时候，最多可以选择多少个砝码
    # 用dp[i] = max(dp[i], dp[i - A[j]] + 1)来更新dp[i]
    # 由于我们最多只能选择3个砝码，因此我们只需要更新dp[i] 3次
    # 最后dp[W]就是答案
    dp = [0] * (W + 1)
    for i in range(N):
        for j in range(W, A[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - A[i]] + 1)
            if j - A[i] > 0:
                dp[j] = max(dp[j], dp[j - A[i]] + 1)
                if j - A[i] - A[i] > 0:
                    dp[j] = max(dp[j], dp[j - A[i] - A[i]] + 1)

    print(dp[W])
