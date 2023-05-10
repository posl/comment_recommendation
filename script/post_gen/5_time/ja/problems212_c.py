Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    ans = 10**9
    for a in A:
        idx = bisect.bisect_left(B, a)
        if idx < M:
            ans = min(ans, abs(a - B[idx]))
        if idx > 0:
            ans = min(ans, abs(a - B[idx - 1]))
    print(ans)

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    #print(a)
    #print(b)
    min_diff = 10**9
    for i in range(n):
        min_diff = min(min_diff,abs(a[i]-b[0]))
        min_diff = min(min_diff,abs(a[i]-b[m-1]))
    for j in range(m):
        min_diff = min(min_diff,abs(a[0]-b[j]))
        min_diff = min(min_diff,abs(a[n-1]-b[j]))
    print(min_diff)
    return

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # a, b をソート
    a.sort()
    b.sort()

    # a, b の要素の差の絶対値の最小値を求める
    ans = 10**9
    i = 0
    j = 0
    while i < n and j < m:
        ans = min(ans, abs(a[i]-b[j]))
        if a[i] > b[j]:
            j += 1
        else:
            i += 1

    print(ans)

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort()
    b.sort()

    min_distance = 10**9

    for i in range(n):
        for j in range(m):
            if abs(a[i]-b[j]) < min_distance:
                min_distance = abs(a[i]-b[j])

    print(min_distance)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort()
    b.sort()

    ans = 10**9
    for i in a:
        l = 0
        r = m-1
        while l <= r:
            mid = (l+r)//2
            if b[mid] < i:
                l = mid+1
            else:
                r = mid-1
        if l < m:
            ans = min(ans,abs(i-b[l]))
        if r >= 0:
            ans = min(ans,abs(i-b[r]))
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a_list.sort()
    b_list.sort()
    ans = 10**9
    for a in a_list:
        for b in b_list:
            ans = min(ans, abs(a-b))
    print(ans)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    ans = 10**9
    i,j = 0,0
    while i < n and j < m:
        ans = min(ans,abs(a[i]-b[j]))
        if a[i] == b[j]:
            break
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    print(ans)

=======
Suggestion 8

def main():
    import sys
    import bisect
    readline = sys.stdin.readline

    n, m = map(int, readline().split())
    a = list(map(int, readline().split()))
    b = list(map(int, readline().split()))

    a.sort()
    b.sort()

    ans = float('inf')
    for i in a:
        idx = bisect.bisect_left(b, i)
        if idx < m:
            ans = min(ans, abs(i - b[idx]))
        if idx > 0:
            ans = min(ans, abs(i - b[idx - 1]))

    print(ans)

=======
Suggestion 9

def solve():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    ans = 10**10
    for i in range(n):
        l = 0
        r = m-1
        while l+1 < r:
            mid = (l+r)//2
            if b[mid] >= a[i]:
                r = mid
            else:
                l = mid
        ans = min(ans, abs(a[i]-b[l]))
        ans = min(ans, abs(a[i]-b[r]))
    print(ans)

=======
Suggestion 10

def solve():
    # 整数 1 つ
    #n = int(input())
    # 整数複数個
    #n, m = map(int, input().split())
    # 整数複数個（リスト）
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    i = 0
    j = 0
    ans = 10**9 + 1
    while i < n and j < m:
        ans = min(ans, abs(a[i]-b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1

    print(ans)
