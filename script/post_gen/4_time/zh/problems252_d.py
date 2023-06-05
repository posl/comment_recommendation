Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if a[i]!=a[j] and a[j]!=a[k] and a[i]!=a[k]:
                    if a[i]+a[j]>a[k]:
                        ans += 1
                    else:
                        break
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    dp = [0 for _ in range(n)]
    dp[0] = 0
    dp[1] = 0
    dp[2] = 0
    for i in range(3, n):
        dp[i] = dp[i-1]
        for j in range(i-1):
            for k in range(j+1, i):
                if A[j] < A[k] < A[i]:
                    dp[i] += 1
    print(dp[n-1])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if a[i] != a[j] and a[j] != a[k] and a[i] != a[k]:
                    if a[i] + a[j] > a[k]:
                        cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if a[i] != a[j] and a[j] != a[k] and a[k] != a[i]:
                    ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 1. 统计A中各个元素出现的次数
    # 2. 统计满足条件的三元组个数
    # 3. 打印答案

    # 1. 统计A中各个元素出现的次数
    count = {}
    for i in range(N):
        if A[i] in count:
            count[A[i]] += 1
        else:
            count[A[i]] = 1

    # 2. 统计满足条件的三元组个数
    # 2.1. 满足条件的三元组个数 = 满足条件的三元组个数 - 满足条件的三元组个数
    # 2.2. 满足条件的三元组个数 = 满足条件的三元组个数 + 满足条件的三元组个数
    # 2.3. 满足条件的三元组个数 = 满足条件的三元组个数 + 满足条件的三元组个数
    # 2.4. 满足条件的三元组个数 = 满足条件的三元组个数 + 满足条件的三元组个数
    # 2.5. 满足条件的三元组个数 = 满足条件的三元组个数 + 满足条件的三元组个数
    # 2.6. 满足条件的三元组个数 = 满足条件的三元组个数 + 满足条件的三元组个数
    # 2.7. 满足条件的三元组个数 = 满足条件的三元组个数 + 满足条件的三元组个数
    # 2.8. 满足条件的三元组个数 = 满

=======
Suggestion 7

def solve(N, A):
    # 请在此添加代码
    cnt = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[i] != A[k]:
                    cnt += 1
    return cnt

=======
Suggestion 8

def solve(n, a):
    from collections import Counter
    a = Counter(a)
    a = sorted(a.items(), key=lambda x: x[0])
    ans = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if a[i][0] != a[j][0] and a[j][0] != a[k][0] and a[i][0] != a[k][0]:
                    ans += a[i][1] * a[j][1] * a[k][1]
    return ans

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    count = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    count += 1
    print(count)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                continue
            for k in range(j+1, n):
                if a[j] == a[k] or a[i] == a[k]:
                    continue
                if a[i] + a[j] > a[k]:
                    ans += 1
                else:
                    break
    print(ans)
