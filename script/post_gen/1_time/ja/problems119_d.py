Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, q = map(int, input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    x = [int(input()) for _ in range(q)]

    import bisect

    ss = [-float("inf")] + s + [float("inf")]
    tt = [-float("inf")] + t + [float("inf")]

    for xx in x:
        i = bisect.bisect_right(ss, xx)
        j = bisect.bisect_right(tt, xx)
        res = float("inf")
        for s1 in [ss[i - 1], ss[i]]:
            for t1 in [tt[j - 1], tt[j]]:
                d1 = abs(xx - s1) + abs(s1 - t1)
                d2 = abs(xx - t1) + abs(t1 - s1)
                res = min(res, d1, d2)
        print(res)

=======
Suggestion 2

def main():
    A,B,Q = map(int,input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    for i in range(Q):
        ans = 10**20
        for j in range(A):
            for k in range(B):
                ans = min(ans,abs(x[i]-s[j])+abs(s[j]-t[k]),abs(x[i]-t[k])+abs(t[k]-s[j]))
        print(ans)

=======
Suggestion 3

def main():
    A,B,Q = map(int,input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]

    import bisect
    for i in range(Q):
        s1 = bisect.bisect_left(s,x[i])
        t1 = bisect.bisect_left(t,x[i])
        s2 = bisect.bisect_right(s,x[i])
        t2 = bisect.bisect_right(t,x[i])

        if s1 == 0 and t1 == 0:
            print(max(s[s1],t[t1]) - x[i])
        elif s1 == A and t1 == B:
            print(x[i] - min(s[s1-1],t[t1-1]))
        elif s1 == 0:
            print(min(max(s[s1],t[t1]) - x[i],x[i] - t[t1-1] + max(s[s1],t[t1]) - t[t1-1]))
        elif t1 == 0:
            print(min(max(s[s1],t[t1]) - x[i],x[i] - s[s1-1] + max(s[s1],t[t1]) - s[s1-1]))
        elif s1 == A:
            print(min(x[i] - min(s[s1-1],t[t1-1]) + min(s[s1-1],t[t1-1]) - s[s1-1],x[i] - max(s[s1-1],t[t1-1]) + max(s[s1-1],t[t1-1]) - s[s1-1]))
        elif t1 == B:
            print(min(x[i] - min(s[s1-1],t[t1-1]) + min(s[s1-1],t[t1-1]) - t[t1-1],x[i] - max(s[s1-1],t[t1-1]) + max(s[s1-1],t[t1-1]) - t[t1-1]))
        else:
            print(min(max(s[s1],t[t1]) - x[i],x[i] - s[s1-1] + max(s[s1],t[t1]) - s[s1-1],

=======
Suggestion 4

def main():
    A,B,Q = map(int,input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    S.sort()
    T.sort()
    import bisect
    for x in X:
        i = bisect.bisect_left(S,x)
        j = bisect.bisect_left(T,x)
        ans = 10**18
        for s in [S[i-1],S[i]]:
            for t in [T[j-1],T[j]]:
                d1,d2 = abs(s-x)+abs(t-s),abs(t-x)+abs(s-t)
                ans = min(ans,d1,d2)
        print(ans)

=======
Suggestion 5

def main():
    a,b,q = map(int,input().split())
    s = [int(input()) for i in range(a)]
    t = [int(input()) for i in range(b)]
    x = [int(input()) for i in range(q)]
    s.insert(0,0)
    s.append(10000000000000000000)
    t.insert(0,0)
    t.append(10000000000000000000)
    import bisect
    for i in x:
        si = bisect.bisect_left(s,i)
        ti = bisect.bisect_left(t,i)
        ans = 10000000000000000000
        for sj in (s[si-1],s[si]):
            for tj in (t[ti-1],t[ti]):
                ans = min(ans,abs(i-sj)+abs(sj-tj),abs(i-tj)+abs(tj-sj))
        print(ans)
main()

=======
Suggestion 6

def main():
    A,B,Q=map(int,input().split())
    S=[int(input())for _ in range(A)]
    T=[int(input())for _ in range(B)]
    X=[int(input())for _ in range(Q)]
    from bisect import bisect_left,bisect_right
    for x in X:
        s=S[bisect_left(S,x)]
        t=T[bisect_left(T,x)]
        sl=s-x if bisect_left(S,x)>0 else float('inf')
        sr=x-s if bisect_left(S,x)<A else float('inf')
        tl=t-x if bisect_left(T,x)>0 else float('inf')
        tr=x-t if bisect_left(T,x)<B else float('inf')
        print(min(max(sl,tl),max(sr,tr),sl+tr+min(sl,tr),sr+tl+min(sr,tl)))
main()

=======
Suggestion 7

def binary_search(list, value):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == value:
            return mid
        elif list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return left

=======
Suggestion 8

def solve():
    from bisect import bisect_left,bisect_right
    a,b,q = map(int,input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    x = [int(input()) for _ in range(q)]
    s.append(10**11)
    t.append(10**11)
    s.append(-10**11)
    t.append(-10**11)
    s.sort()
    t.sort()
    for i in range(q):
        ans = 10**11
        si = bisect_right(s,x[i])
        sj = bisect_left(s,x[i])
        ti = bisect_right(t,x[i])
        tj = bisect_left(t,x[i])
        for j in [si,sj]:
            for k in [ti,tj]:
                ans = min(ans,abs(x[i]-s[j])+abs(s[j]-t[k]),abs(x[i]-t[k])+abs(t[k]-s[j]))
        print(ans)

=======
Suggestion 9

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while True:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            if right == mid:
                return mid
            right = mid
        elif arr[mid] < target:
            if left == mid:
                return mid + 1
            left = mid

=======
Suggestion 10

def solve():
    # 二分探索
    # ある地点から東に移動するときに通過する神社と寺の最小値を求める
    # ある地点から西に移動するときに通過する神社と寺の最小値を求める
    # 二分探索で解く
    # 東西それぞれの最小値を求める
    # 二分探索で解く
    # ある地点から東に移動するときに通過する神社と寺の最小値を求める
    # ある地点から西に移動するときに通過する神社と寺の最小値を求める
    # 二分探索で解く
    # 東西それぞれの最小値を求める
    # 二分探索で解く
    # ある地点から東に移動するときに通過する神社と寺の最小値を求める
    # ある地点から西に移動するときに通過する神社と寺の最小値を求める
    # 二分探索で解く
    # 東西それぞれの最小値を求める
    # 二分探索で解く
    # ある地点から東に移動するときに通過する神社と寺の最小値を求める
    # ある地点から西に移動するときに通過する神社と寺の最小値を求める
    # 二分探索で解く
    # 東西それぞれの最小値を求める
    # 二分探索で解く
    # ある地点から東に移動するときに通過する神社と
