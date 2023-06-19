Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    a = [0]*(n+1)
    for i in range(m):
        a[int(input())]=1
    a[0]=1
    a[1]=0
    for i in range(2,n+1):
        if a[i]==1:
            a[i]=0
        else:
            a[i]=a[i-1]+a[i-2]
            a[i]%=1000000007
    print(a[n])

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def climb_stairs(n, m, a):
    if m == 0:
        return 1

    a.append(n)
    a.insert(0, 0)
    result = 1
    for i in range(1, m + 2):
        result *= (a[i] - a[i - 1])

    return result % 1000000007

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    broken = set()
    for _ in range(M):
        broken.add(int(input()))

    dp = [0 for _ in range(N+1)]
    dp[0] = 1
    if 1 not in broken:
        dp[1] = 1

    for i in range(2, N+1):
        if i not in broken:
            dp[i] = dp[i-1] + dp[i-2]

    print(dp[N] % 1000000007)

=======
Suggestion 5

def main():
    N,M = list(map(int,input().split()))
    a = []
    for i in range(M):
        a.append(int(input()))
    a.append(N+1)
    dp = [0 for i in range(N+1)]
    dp[0] = 1
    for i in range(1,N+1):
        if i in a:
            continue
        if i == 1:
            dp[i] = dp[i-1]
        else:
            dp[i] = (dp[i-2] + dp[i-1]) % 1000000007
    print(dp[N])

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = []
    for i in range(m):
        a.append(int(input()))
    a.append(n)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if i not in a:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    print(dp[n])

=======
Suggestion 7

def problems129_c():
    n,m = map(int,input().split())
    a = [0]
    for i in range(m):
        a.append(int(input()))
    a.append(n+1)
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        dp[i] = dp[i-1]
        for j in range(1,m+1):
            if a[j] == i:
                dp[i] = 0
                break
            elif a[j] > i:
                break
            else:
                dp[i] = (dp[i]+dp[i-a[j]-1])%1000000007
    print(dp[n])

=======
Suggestion 8

def main():
    # 读取输入
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    # 从第0阶开始爬楼梯
    dp = [0] * (n + 1)
    dp[0] = 1
    # 爬楼梯
    for i in range(1, n + 1):
        if i not in a:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    # 打印结果
    print(dp[n])

=======
Suggestion 9

def problems129_c():
    pass
