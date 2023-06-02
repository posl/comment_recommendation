Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort()
    p = p[-k:]
    print((sum(p)+k)/2)

main()

=======
Suggestion 3

def main():
    n, k = list(map(int, input().split()))
    p = list(map(int, input().split()))
    p = [0] + p
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + p[i + 1]
    ans = 0
    for i in range(n - k + 1):
        ans = max(ans, (s[i + k] - s[i]) / 2 + s[i])
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    ans = sum(p[-k:])
    print(ans / 2)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [0] + P
    for i in range(1, N+1):
        P[i] += P[i-1]
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, (P[i+K] - P[i]) / 2 + P[i])
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(k):
        ans += (p[i]+1)/2
    tmp = ans
    for i in range(k,n):
        tmp = tmp + (p[i]+1)/2 - (p[i-k]+1)/2
        ans = max(ans,tmp)
    print(ans)

=======
Suggestion 7

def max_expected_value(n, k, p):
    p_sum = sum(p[0:k])
    max_sum = p_sum
    for i in range(k, n):
        p_sum += p[i] - p[i-k]
        if p_sum > max_sum:
            max_sum = p_sum
    return (max_sum + k)/2

=======
Suggestion 8

def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    p.reverse()
    ans = 0
    for i in range(k):
        ans += p[i]
    ans += k
    ans /= 2
    print(ans)

=======
Suggestion 9

def solve():
    #解法
    #1. 从左到右，依次找出最大的k个数，求和，即为所求
    #2. 从左到右，依次找出最大的k个数，求和，然后依次找出最大的k-1个数，求和，然后依次找出最大的k-2个数，求和，...，直到最后一个数，求和，取最大值，即为所求
    #3. 从左到右，依次找出最大的k个数，求和，然后依次找出最大的k-1个数，求和，然后依次找出最大的k-2个数，求和，...，直到最后一个数，求和，取最大值，然后从右到左，依次找出最大的k个数，求和，然后依次找出最大的k-1个数，求和，然后依次找出最大的k-2个数，求和，...，直到最后一个数，求和，取最大值，即为所求
    #4. 从左到右，依次找出最大的k个数，求和，然后从右到左，依次找出最大的k个数，求和，取最大值，即为所求
    #5. 从右到左，依次找出最大的k个数，求和，取最大值，即为所求
    #6. 从右到左，依次找出最大的k个数，求和，然后从左到右，依次找出最大的k个数，求和，取最大值，即为所求
    #7. 从右到左，依次找出最大的k个数，求和，然后从左到右，依次找出最大的k-1个数，求和，然后从右到左，依次找出最大的k个数
