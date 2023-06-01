Synthesizing 10/10 solutions

=======
Suggestion 1

def problems256_d():
    pass

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    for _ in range(n):
        l, r = map(int, input().split())
        a.append((l, r))
    a.sort()
    ans = []
    l, r = a[0]
    for i in range(1, n):
        if a[i][0] <= r:
            r = max(r, a[i][1])
        else:
            ans.append((l, r))
            l, r = a[i]
    ans.append((l, r))
    for l, r in ans:
        print(l, r)

=======
Suggestion 3

def main():
    n = int(input())
    intervals = []
    for i in range(n):
        l, r = map(int, input().split())
        intervals.append((l, r))
    intervals.sort()
    l, r = intervals[0]
    for i in range(1, n):
        if intervals[i][0] <= r:
            r = max(intervals[i][1], r)
        else:
            print(l, r)
            l, r = intervals[i]
    print(l, r)

=======
Suggestion 4

def merge_intervals(intervals):
    # 先排序
    intervals.sort(key=lambda x: x[0])
    # print(intervals)
    merged = []
    for interval in intervals:
        # 如果列表为空，或者当前区间与上一区间不重合，直接添加
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
            # 否则的话，我们就可以与上一区间进行合并
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

=======
Suggestion 5

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort()
    ans = []
    ans.append(l[0])
    for i in range(1,n):
        if ans[-1][1] < l[i][0]:
            ans.append(l[i])
        elif ans[-1][1] < l[i][1]:
            ans[-1][1] = l[i][1]
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1])

=======
Suggestion 6

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
    return merged

=======
Suggestion 7

def main():
    n = int(input())
    lr = []
    for _ in range(n):
        lr.append(tuple(map(int, input().split())))
    lr.sort(key=lambda x: x[0])
    l, r = lr[0]
    for i in range(1, n):
        if lr[i][0] <= r:
            r = max(r, lr[i][1])
        else:
            print(l, r)
            l, r = lr[i]
    print(l, r)

=======
Suggestion 8

def main():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    print(L[0], R[N-1])

=======
Suggestion 9

def main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    data.sort()
    left = data[0][0]
    right = data[0][1]
    for i in range(1, n):
        if data[i][0] <= right:
            if data[i][1] > right:
                right = data[i][1]
        else:
            print(left, right)
            left = data[i][0]
            right = data[i][1]
    print(left, right)

=======
Suggestion 10

def main():
    n = int(input())
    l = []
    r = []
    for i in range(n):
        ll, rr = map(int, input().split())
        l.append(ll)
        r.append(rr)
    l.sort()
    r.sort()
    l.append(0)
    r.append(0)
    ans = 0
    for i in range(n):
        if l[i+1] > r[i]:
            ans += 1
    print(ans)
