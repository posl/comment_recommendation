Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    for i in range(k-1,n):
        print(sorted(p[:i+1],reverse=True)[k-1])

=======
Suggestion 2

def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    for i in range(K-1,N):
        print(sorted(P[:i+1])[K-1])

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(K-1, N):
        print(sorted(P[:i+1])[-K+1])

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(k-1, n):
        print(sorted(p[:i+1])[-k+1])

=======
Suggestion 6

def solve(n,k,nums):
    # 从中间开始比较，找到第k大的数
    # 从中间开始比较，找到第k大的数
    def findKth(nums,k):
        if len(nums)==1:
            return nums[0]
        mid = len(nums)//2
        left = [i for i in nums if i<nums[mid]]
        right = [i for i in nums if i>nums[mid]]
        if len(right)>=k:
            return findKth(right,k)
        elif len(right)==k-1:
            return nums[mid]
        else:
            return findKth(left,k-len(right)-1)
    for i in range(k,n+1):
        print(findKth(nums[:i],k))

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    if k == 1:
        print(min(p))
        return
    if k == n:
        print(max(p))
        return
    for i in range(n - k + 1):
        print(max(p[i:i + k]))

=======
Suggestion 9

def solve():
    from heapq import heappop, heappush
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    Q = []
    for i in range(K):
        heappush(Q, (-P[i], i))
    print(-Q[0][0])
    for i in range(K, N):
        heappush(Q, (-P[i], i))
        while Q[0][1] <= i - K:
            heappop(Q)
        print(-Q[0][0])
