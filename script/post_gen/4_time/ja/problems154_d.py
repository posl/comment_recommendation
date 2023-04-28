Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, sum(p[i:i+K]) / 2 + 0.5 * K)
    print(ans)

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(k):
        ans += (p[i]+1)/2
    tmp = ans
    for i in range(k,n):
        tmp -= (p[i-k]+1)/2
        tmp += (p[i]+1)/2
        ans = max(ans,tmp)
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))

    p_sum = [0] * (N+1)
    for i in range(N):
        p_sum[i+1] = p_sum[i] + p[i]

    max_sum = 0
    for i in range(N-K+1):
        sum = p_sum[i+K] - p_sum[i]
        if sum > max_sum:
            max_sum = sum

    print((max_sum + K)/2)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    pl = list(map(int,input().split()))
    psum = [0]*(n+1)
    for i in range(n):
        psum[i+1] = psum[i] + pl[i]
    ans = 0
    for i in range(n-k+1):
        ans = max(ans,(psum[i+k]-psum[i])/2)
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p_max = sum(p[:k])
    p_sum = p_max
    for i in range(n-k):
        p_sum = p_sum - p[i] + p[i+k]
        if p_sum > p_max:
            p_max = p_sum
    print((p_max+k)/2)

=======
Suggestion 6

def solve(N, K, p):
    s = 0
    for i in range(K):
        s += p[i]
    m = s
    for i in range(K, N):
        s -= p[i-K]
        s += p[i]
        m = max(m, s)
    return (m + K) / 2

N, K = map(int, input().split())
p = list(map(int, input().split()))
print(solve(N, K, p))

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    ans = 0
    for i in range(K):
        ans += (P[i]+1)/2
    temp = ans
    for i in range(1,N-K+1):
        temp -= (P[i-1]+1)/2
        temp += (P[i+K-1]+1)/2
        if temp > ans:
            ans = temp
    print(ans)

=======
Suggestion 8

def solve():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    psum = [0]
    for i in range(N):
        psum.append(psum[i]+p[i])
    ans = 0
    for i in range(N-K+1):
        ans = max(ans,(psum[i+K]-psum[i])/2+K/2)
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    p_list = list(map(int, input().split()))
    p_list = [0] + p_list

    sum_list = [0]
    for i in range(N):
        sum_list.append(sum_list[i] + p_list[i+1])

    max_sum = 0
    for i in range(N-K+1):
        max_sum = max(max_sum, sum_list[i+K] - sum_list[i])

    print((max_sum + K) / 2)

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))

    #i番目のサイコロを振った時の期待値
    e = [0 for _ in range(N)]
    for i in range(N):
        e[i] = (p[i]+1)/2
    #print(e)

    #累積和
    s = [0 for _ in range(N+1)]
    for i in range(N):
        s[i+1] = s[i]+e[i]
    #print(s)

    ans = 0
    for i in range(N-K+1):
        ans = max(ans,s[i+K]-s[i])
    print(ans)
