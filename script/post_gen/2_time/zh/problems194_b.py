Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    print(min([max(a[i], b[i]) for i in range(n)]))
    
main()

=======
Suggestion 2

def min_time(N, A, B):
    min_time = 1000000000
    for i in range(N):
        for j in range(N):
            if i != j:
                min_time = min(min_time, max(A[i], B[j]))
            else:
                min_time = min(min_time, A[i] + B[j])
    return min_time

N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

print(min_time(N, A, B))

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_time = 10**10
    for i in range(N):
        for j in range(N):
            if i == j:
                time = A[i] + B[j]
            else:
                time = max(A[i], B[j])
            if time < min_time:
                min_time = time
    print(min_time)

=======
Suggestion 4

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 10**10
    for i in range(N):
        for j in range(N):
            if i == j:
                ans = min(ans, A[i]+B[j])
            else:
                ans = min(ans, max(A[i], B[j]))
    print(ans)

=======
Suggestion 5

def get_result(n, a, b):
    # 1. 每个任务的最优解
    # 2. 两个任务的最优解
    # 3. 三个任务的最优解
    # 4. ...
    # 每个任务的最优解 = min(完成任务A的时间，完成任务B的时间)
    # 两个任务的最优解 = min(完成任务A的时间，完成任务B的时间)，两个任务分配给同一个人
    # 三个任务的最优解 = min(完成任务A的时间，完成任务B的时间)，三个任务分配给同一个人
    # ...
    # 这样的话，我们就可以得到一个动态规划的解法
    # dp[i] = min(dp[i-1] + a[i], dp[i-2] + b[i])
    # dp[0] = a[0], dp[1] = min(a[0] + a[1], b[0])
    # dp[i]表示前i个任务的最优解
    # dp[i-1] + a[i]表示第i个任务分配给一个人，前i-1个任务分配给另一个人
    # dp[i-2] + b[i]表示第i个任务分配给另一个人，前i-2个任务分配给另一个人
    dp = [0 for i in range(n)]
    dp[0] = a[0]
    dp[1] = min(a[0] + a[1], b[0])
    for i in range(2, n):
        dp[i] = min(dp[i-1] + a[i], dp[i-2] + b[i-1])
    return dp[n-1]

n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]
for i in range(n):
    a[i], b[i] = map(int, input().split())
print(get_result(n, a, b))

=======
Suggestion 6

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    print(min(A[N-1], B[N-1]))

=======
Suggestion 7

def find_min_time(n, a, b):
    min_time = 1000000
    for i in range(n):
        for j in range(n):
            if i == j:
                time = a[i] + b[j]
            else:
                time = max(a[i], b[j])
            if time < min_time:
                min_time = time
    return min_time

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    min_time = 1000000
    for i in range(n):
        for j in range(n):
            if i == j:
                min_time = min(min_time, a[i]+b[j])
            else:
                min_time = min(min_time, max(a[i], b[j]))
    print(min_time)

=======
Suggestion 9

def find_min_time():
    # 读取输入数据
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    # 计算最短时间
    min_time = max(a[0], b[0])
    for i in range(1, n):
        time = max(a[i], b[i])
        if time < min_time:
            min_time = time

    # 输出结果
    print(min_time)

=======
Suggestion 10

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    min_time = 10**6
    for i in range(n):
        for j in range(n):
            if i == j:
                time = a[i] + b[j]
            else:
                time = max(a[i], b[j])
            if time < min_time:
                min_time = time
    print(min_time)
