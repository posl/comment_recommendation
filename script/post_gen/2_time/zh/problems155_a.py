Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    sum = 0
    for i in range(k):
        sum += p[i]
    max = sum
    for i in range(k, n):
        sum = sum - p[i-k] + p[i]
        if sum > max:
            max = sum
    print((max + k)/2)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    for i in range(1, n + 1):
        p[i] += p[i - 1]
    ans = 0
    for i in range(k, n + 1):
        ans = max(ans, p[i] - p[i - k])
    print((ans + k) / 2)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    #print(n,k,p)
    psum = [0] * (n+1)
    for i in range(n):
        psum[i+1] = psum[i] + p[i]
    #print(psum)
    ans = 0
    for i in range(n-k+1):
        ans = max(ans,(psum[i+k]-psum[i]+k)/2)
    print(ans)

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    sum_p = [0]*(N+1)
    for i in range(N):
        sum_p[i+1] = sum_p[i] + p[i]
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, (sum_p[i+K]-sum_p[i])/2 + sum_p[i])
    print(ans)

=======
Suggestion 5

def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    sum_p = sum(p[:k])
    max_sum_p = sum_p
    for i in range(k,n):
        sum_p = sum_p - p[i-k] + p[i]
        if sum_p > max_sum_p:
            max_sum_p = sum_p
    print((max_sum_p+k)/2)

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    # 读入数据
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    # 计算答案
    s = sum(p[:k])
    ans = s
    for i in range(k, n):
        s += p[i] - p[i-k]
        ans = max(ans, s)

    # 打印答案
    print((ans + k) / 2)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    max_sum = 0
    for i in range(n-k+1):
        sum = 0
        for j in range(i,i+k):
            sum += p[j]
        if max_sum < sum:
            max_sum = sum
    print((max_sum+k)/2)

=======
Suggestion 9

def solve():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        ans += (p[i] + 1) / 2
    cur = ans
    for i in range(K, N):
        cur += (p[i] + 1) / 2
        cur -= (p[i - K] + 1) / 2
        ans = max(ans, cur)
    print(ans)

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    s = sum(p[:k])
    ans = s
    for i in range(n-k):
        s = s - p[i] + p[i+k]
        ans = max(ans,s)
    print((ans+k)/2)
