Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,l,r = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        a[i] = a[i] + l
    ans = 0
    for i in range(n):
        ans += a[i]
    a.sort()
    for i in range(n):
        if a[i] > 0:
            break
        if i % 2 == 1:
            ans -= 2 * a[i]
    print(ans)

=======
Suggestion 2

def solve():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    # dp[i][0] 表示第i个元素被替换的情况下的最小值
    # dp[i][1] 表示第i个元素不被替换的情况下的最小值
    dp = [[0 for _ in range(2)] for _ in range(N+1)]
    dp[1][0] = L
    dp[1][1] = 0

    for i in range(2, N+1):
        dp[i][0] = min(dp[i-1][0] + L, dp[i-1][1] + L)
        dp[i][1] = min(dp[i-1][0] + R, dp[i-1][1] + R)

    ans = float('inf')
    for i in range(1, N+1):
        ans = min(ans, dp[i][0]+(N-i)*R+A[i-1], dp[i][1]+(N-i)*R+A[i-1])

    print(ans)

=======
Suggestion 3

def solve():
    n,l,r=map(int,input().split())
    a=list(map(int,input().split()))
    ans=sum(a)
    for i in range(1,n):
        a[i]=min(a[i-1]*2,l+r)
    for i in range(n-1,-1,-1):
        if i<n-1:
            a[i]=min(a[i],a[i+1]*2)
        ans+=a[i]
    print(ans)

solve()

=======
Suggestion 4

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if i > 0:
            a[i] += a[i-1]
    ans = 0
    minsum = 0
    for i in range(n):
        if i > 0:
            minsum = min(minsum, a[i-1])
        if a[i]-minsum < 0:
            ans += l*(a[i]-minsum)
        else:
            ans += r*(a[i]-minsum)
    print(ans)

=======
Suggestion 5

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_sum(a, n, l, r))

=======
Suggestion 6

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * pow(L, i) + A[i] * pow(R, N - i - 1)
    print(ans)

=======
Suggestion 7

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    
    ans = 0
    for i in range(n):
        if a[i] < 0:
            a[i] = -a[i]
            ans += l
        else:
            ans += r
    
    a.sort()
    
    if n % 2 == 1:
        ans -= 2 * min(a[0], a[n // 2])
    
    print(ans)

=======
Suggestion 8

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    min_sum = 0
    for i in range(n):
        a[i] = a[i] + l
        if a[i] < l:
            a[i] = l
        elif a[i] > r:
            a[i] = r
        min_sum += a[i]
    print(min_sum)

=======
Suggestion 9

def get_min_sum(n, l, r, a):
    min_sum = 0
    min_sum += a[0] * l
    for i in range(1, n):
        if a[i] < a[i-1]:
            min_sum += a[i] * l
        else:
            min_sum += a[i] * r
    return min_sum

n, l, r = map(int, input().split())
a = list(map(int, input().split()))
print(get_min_sum(n, l, r, a))

=======
Suggestion 10

def main():
    N,L,R = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A.reverse()
    #print(A)
    sum = 0
    for i in range(N):
        if i < L:
            sum += A[i]
        else:
            sum += A[L-1]
    print(sum)
