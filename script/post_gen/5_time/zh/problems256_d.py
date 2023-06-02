Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    L.sort()
    R.sort()

    ans = 0
    cur = 0
    for i in range(N):
        if cur < L[i]:
            ans += 1
            cur = R[i]
        else:
            cur = max(cur, R[i])

    ans += 1
    print(ans)

solve()

=======
Suggestion 2

def problems256_d():
    pass

=======
Suggestion 3

def main():
    n = int(input())
    intervals = list()
    for i in range(n):
        line = input().split()
        intervals.append((int(line[0]), int(line[1])))
    intervals.sort(key=lambda x: x[0])
    tmp = intervals[0]
    ans = list()
    for i in range(1, n):
        if tmp[1] >= intervals[i][0]:
            tmp = (tmp[0], max(tmp[1], intervals[i][1]))
        else:
            ans.append(tmp)
            tmp = intervals[i]
    ans.append(tmp)
    for i in range(len(ans)):
        print("{} {}".format(ans[i][0], ans[i][1]))

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    for i in range(n):
        l, r = map(int, input().split())
        a.append([l, r])
    a.sort(key=lambda x: x[0])
    ans = [[a[0][0], a[0][1]]]
    for i in range(1, n):
        if ans[-1][1] < a[i][0]:
            ans.append([a[i][0], a[i][1]])
        else:
            ans[-1][1] = max(ans[-1][1], a[i][1])
    for i in ans:
        print(i[0], i[1])

=======
Suggestion 5

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
    print(L[0], R[-1])

=======
Suggestion 6

def main():
    n = int(input())
    l = []
    r = []
    for i in range(n):
        a, b = map(int, input().split())
        l.append(a)
        r.append(b)

    l.sort()
    r.sort()

    print(l[0], r[-1])

=======
Suggestion 7

def main():
    n = int(input())
    lr = [list(map(int, input().split())) for _ in range(n)]
    lr.sort(key=lambda x: x[0])
    ans = []
    l = lr[0][0]
    r = lr[0][1]
    for i in range(1, n):
        if lr[i][0] <= r:
            r = max(r, lr[i][1])
        else:
            ans.append([l, r])
            l = lr[i][0]
            r = lr[i][1]
    ans.append([l, r])
    for a in ans:
        print(*a)

=======
Suggestion 8

def merge(arr):
    arr.sort()
    i = 0
    while i < len(arr) - 1:
        if arr[i][1] >= arr[i+1][0]:
            arr[i][1] = max(arr[i][1], arr[i+1][1])
            arr.pop(i+1)
        else:
            i += 1
    return arr

=======
Suggestion 9

def main():
    n = int(input())
    L = [0]*n
    R = [0]*n
    for i in range(n):
        L[i],R[i] = map(int,input().split())
    L.sort()
    R.sort()
    for i in range(n-1):
        if R[i] < L[i+1]:
            print(L[i],R[i])
            print(L[i+1],R[i+1])
            return
    print(L[0],R[-1])
    return
