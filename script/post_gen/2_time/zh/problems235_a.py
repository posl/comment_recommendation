Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n,k,p):
    ans=[]
    for i in range(k,n+1):
        ans.append(max(p[i-k:i]))
    print(*ans,sep='\n')

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n-k+1):
        print(max(a[i:i+k]))

=======
Suggestion 3

def max_k(n, k, arr):
    from collections import deque
    d = deque()
    for i in range(n):
        while d and arr[d[-1]] <= arr[i]:
            d.pop()
        d.append(i)
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            print(arr[d[0]])

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(K-1, N):
        print(sorted(P[:i+1], reverse=True)[K-1])

=======
Suggestion 5

def func():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(k-1, n):
        print(sorted(p[:i+1], reverse=True)[k-1])

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    for i in range(k-1,n):
        print(sorted(p[:i+1])[-k+1])

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    for i in range(k,n+1):
        print(sorted(p[:i])[-k])

=======
Suggestion 8

def solve(n, k, p):
    #print(n, k, p)
    #print(p[0:k-1])
    #print(p[k-1:n])
    for i in range(k-1, n):
        print(sorted(p[0:i+1])[k-1])
    return 0

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(K-1, N):
        print(sorted(P[:i+1])[-1])
    return

=======
Suggestion 10

def solve(n,k,nums):
    # k-1个最大数
    res = []
    for i in range(k-1,n):
        res.append(max(nums[i-k+1:i+1]))
    return res
