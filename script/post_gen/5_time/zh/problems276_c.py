Synthesizing 10/10 solutions

=======
Suggestion 1

def reverse(s, e, p):
    while s < e:
        p[s], p[e] = p[e], p[s]
        s += 1
        e -= 1

=======
Suggestion 2

def get_min_permutation(n, p):
    p = [int(x) for x in p.split()]
    k = 0
    for i in range(n):
        k += (p[i] - 1) * factorial(n - i - 1)
    k += 1
    q = [0] * n
    used = [False] * n
    for i in range(n):
        for j in range(n):
            if used[j]:
                continue
            q[i] = j + 1
            if factorial(n - i - 1) < k:
                k -= factorial(n - i - 1)
            else:
                used[j] = True
                break
    return q

=======
Suggestion 3

def swap(a, b):
    return b, a

=======
Suggestion 4

def permute(nums):
    res = []
    def backtrack(nums, tmp):
        if not nums:
            res.append(tmp)
            return
        for i in range(len(nums)):
            backtrack(nums[:i]+nums[i+1:], tmp+[nums[i]])
    backtrack(nums, [])
    return res

=======
Suggestion 5

def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    a[i:] = a[len(a)-1:i-1:-1]
    return True

n = int(input())
p = list(map(int, input().split()))
a = list(range(1, n+1))
i = 1
while True:
    if p == a:
        print(*a)
        break
    next_permutation(a)
    i += 1

=======
Suggestion 6

def main():
    N = int(input())
    P = [int(i) for i in input().split()]
    Q = [0] * N
    for i, p in enumerate(P):
        Q[p - 1] = i + 1
    print(*Q)

=======
Suggestion 7

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    print(*Q)

=======
Suggestion 8

def get_input():
    n = int(input())
    p = list(map(int, input().split()))
    return n, p

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p = [0] + p
    q = [0] * (n + 1)
    for i in range(1, n + 1):
        q[p[i]] = i
    print(*q[1:])

=======
Suggestion 10

def solve():
    N = int(input())
    P = list(map(int,input().split()))
    #print(P)
    Q = [0]*N
    for i in range(N):
        Q[P[i]-1] = i+1
    print(*Q)
