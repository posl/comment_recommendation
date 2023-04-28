Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = []
    for i in a:
        ans.append(n-1-d[i]+1)
    print(*ans, sep='\n')

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = {}
    for i in range(n):
        if a[i] in cnt:
            cnt[a[i]] += 1
        else:
            cnt[a[i]] = 1
    ans = 0
    for i in range(n):
        ans += (cnt[a[i]] - 1)
    for i in range(n):
        print(ans - (cnt[a[i]] - 1))

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = {}
    for i in range(n):
        if a[i] in b:
            b[a[i]] += 1
        else:
            b[a[i]] = 1
    ans = [0] * n
    for i in range(n):
        ans[i] = n - b.get(a[i]) + 1
    print('\n'.join(map(str, ans)))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    counter = {}
    for a in A:
        if a not in counter:
            counter[a] = 0
        counter[a] += 1

    for i in range(N):
        if A[i] in counter:
            print(N - counter[A[i]])
        else:
            print(N - 1)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
    ans = [0] * n
    for i in range(n):
        ans[i] = d[a[i]] * (d[a[i]] - 1) // 2
    for i in range(n):
        print(sum(ans) - (d[a[i]] - 1))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[A[i]-1] += 1
    for i in range(N):
        print(ans[i]-1)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0 for _ in range(n+1)]
    for i in range(n):
        cnt[a[i]] += 1
    ans = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        ans[i] = cnt[i] * (cnt[i]-1) // 2
    allsum = sum(ans)
    for i in range(n):
        print(allsum - (cnt[a[i]]-1))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n+1)
    for i in range(n):
        b[a[i]] += 1
    c = [0] * (n+1)
    for i in range(1, n+1):
        c[i] = c[i-1] + b[i] * (b[i]-1) // 2
    for i in range(n):
        print(c[a[i]-1] + (b[a[i]]-1) * (b[a[i]]-2) // 2)

=======
Suggestion 9

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

import math

N = int(input())
A = list(map(int, input().split(" ")))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0 for _ in range(N)]
    for a in A:
        ans[a-1] += 1
    for i in ans:
        print(i)
    return
