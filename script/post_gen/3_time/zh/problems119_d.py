Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    #A,B,Q = map(int,input().split())
    A,B,Q = 2,3,4
    #s = [int(input()) for i in range(A)]
    s = [100,600]
    #t = [int(input()) for i in range(B)]
    t = [400,900,1000]
    #x = [int(input()) for i in range(Q)]
    x = [150,2000,899,799]
    for i in range(Q):
        l = 0
        r = 0
        while l < A and s[l] < x[i]:
            l += 1
        while r < B and t[r] < x[i]:
            r += 1
        ans = 10 ** 20
        for j in range(l-1,l+1):
            for k in range(r-1,r+1):
                d1 = abs(s[j]-x[i]) + abs(t[k]-s[j])
                d2 = abs(t[k]-x[i]) + abs(s[j]-t[k])
                ans = min(ans,d1,d2)
        print(ans)

=======
Suggestion 3

def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1

=======
Suggestion 4

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return low


a, b, q = map(int, input().split())
s = [int(input()) for i in range(a)]
t = [int(input()) for i in range(b)]
x = [int(input()) for i in range(q)]
s.sort()
t.sort()
for i in range(q):
    ans = 10 ** 11
    si = binary_search(s, x[i])
    ti = binary_search(t, x[i])
    for ss in [s[si - 1], s[si]]:
        for tt in [t[ti - 1], t[ti]]:
            ans = min(ans, abs(ss - x[i]) + abs(ss - tt), abs(tt - x[i]) + abs(tt - ss))
    print(ans)

=======
Suggestion 5

def binary_search(a, b, x):
    left = 0
    right = len(a) - 1
    while right - left > 1:
        mid = (left + right) // 2
        if x < a[mid]:
            right = mid
        else:
            left = mid
    return abs(x - a[left]) if abs(x - a[left]) < abs(x - a[right]) else abs(x - a[right])

a, b, q = map(int, input().split())
s = [int(input()) for i in range(a)]
t = [int(input()) for i in range(b)]
x = [int(input()) for i in range(q)]

for i in range(q):
    ans = 10**20
    ans = min(ans, binary_search(s, t, x[i]))
    ans = min(ans, binary_search(t, s, x[i]))
    print(ans)

=======
Suggestion 6

def main():
    a,b,q = map(int,input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    x = [int(input()) for _ in range(q)]

    # 二分探索
    def binary_search(array, value):
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == value:
                return True
            elif array[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        return False

    # 神社と寺の位置を統合
    st = sorted(s + t)

    # クエリに答える
    for i in range(q):
        ans = float("inf")
        # 神社と寺の位置を二分探索
        idx = binary_search(st, x[i])
        # 神社と寺の位置の間の距離を計算
        if not idx:
            idx = st.index(x[i])
            if idx == 0:
                ans = min(ans, abs(st[idx] - x[i]))
            elif idx == len(st):
                ans = min(ans, abs(st[idx - 1] - x[i]))
            else:
                ans = min(ans, abs(st[idx] - x[i]), abs(st[idx - 1] - x[i]))
        # 神社と寺の位置の間の距離を計算
        else:
            ans = 0
        # 神社と寺の位置の間の距離が最小となるものを出力
        print(ans)

=======
Suggestion 7

def binarySearch(array, target):
    #二分查找
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

A, B, Q = map(int, input().split())
S = [int(input()) for i in range(A)]
T = [int(input()) for i in range(B)]
X = [int(input()) for i in range(Q)]
S.sort()
T.sort()
for i in range(Q):
    ans = 10**19
    x = X[i]
    s = binarySearch(S, x)
    t = binarySearch(T, x)
    for s0 in [S[s-1], S[s]]:
        for t0 in [T[t-1], T[t]]:
            d1 = abs(s0 - x) + abs(t0 - s0)
            d2 = abs(t0 - x) + abs(s0 - t0)
            ans = min(ans, d1, d2)
    print(ans)

=======
Suggestion 8

def find(s,t,x):
    if s[0]>x:
        return s[0]-x
    if t[-1]<x:
        return x-t[-1]
    l=0
    r=len(s)-1
    while l<r:
        mid=(l+r)//2
        if s[mid]==x:
            return 0
        elif s[mid]>x:
            r=mid
        else:
            l=mid+1
    if s[l]==x:
        return 0
    else:
        return min(s[l]-x,x-s[l-1])

a,b,q=map(int,input().split())
s=[]
t=[]
for i in range(a):
    s.append(int(input()))
for i in range(b):
    t.append(int(input()))
for i in range(q):
    x=int(input())
    print(min(find(s,t,x),find(t,s,x),find(s,t[x]),find(t,s[x])))

=======
Suggestion 9

def search(list, target):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = int((left + right)/2)
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
