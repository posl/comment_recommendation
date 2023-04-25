Synthesizing 9/10 solutions

=======
Suggestion 1

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
    ans = []
    i = 0
    while i < N:
        l = L[i]
        while i < N and L[i] <= R[i-1]:
            i += 1
        r = R[i-1]
        ans.append([l, r])
    for a in ans:
        print(a[0], a[1])

=======
Suggestion 2

def main():
    N = int(input())
    intervals = []
    for i in range(N):
        L, R = map(int, input().split())
        intervals.append([L, R])
    intervals.sort(key=lambda x: x[0])
    ans = []
    ans.append(intervals[0])
    for i in range(1, N):
        if ans[-1][1] < intervals[i][0]:
            ans.append(intervals[i])
        elif ans[-1][1] < intervals[i][1]:
            ans[-1][1] = intervals[i][1]
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

=======
Suggestion 3

def main():
    n = int(input())
    intervals = []
    for _ in range(n):
        l, r = map(int, input().split())
        intervals.append((l, r))
    intervals.sort()

    ans = []
    for l, r in intervals:
        if not ans or ans[-1][1] < l:
            ans.append((l, r))
        else:
            ans[-1] = (ans[-1][0], max(ans[-1][1], r))

    for l, r in ans:
        print(l, r)

=======
Suggestion 4

def main():
    N = int(input())
    intervals = []
    for _ in range(N):
        l, r = map(int, input().split())
        intervals.append((l, r))
    intervals.sort()
    ans = []
    for l, r in intervals:
        if not ans:
            ans.append((l, r))
            continue
        if ans[-1][1] >= r:
            continue
        if ans[-1][1] >= l:
            ans[-1] = (ans[-1][0], r)
            continue
        ans.append((l, r))
    for l, r in ans:
        print(l, r)

=======
Suggestion 5

def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    ans = []
    for l, r in LR:
        if ans and ans[-1][1] >= l:
            ans[-1][1] = max(ans[-1][1], r)
        else:
            ans.append([l, r])
    for l, r in ans:
        print(l, r)

main()

=======
Suggestion 6

def main():
    N = int(input())
    intervals = []
    for _ in range(N):
        l, r = map(int, input().split())
        intervals.append((l, r))
    intervals.sort()
    ans = []
    for i in range(N):
        l, r = intervals[i]
        if ans and ans[-1][1] >= l:
            ans[-1][1] = max(ans[-1][1], r)
        else:
            ans.append([l, r])
    for a in ans:
        print(a[0], a[1])

=======
Suggestion 7

def main():
    N = int(input())
    intervals = []
    for i in range(N):
        L, R = map(int, input().split())
        intervals.append((L, R))
    intervals.sort()
    ans = []
    left, right = intervals[0]
    for i in range(1, N):
        if right >= intervals[i][0]:
            right = max(right, intervals[i][1])
        else:
            ans.append((left, right))
            left, right = intervals[i]
    ans.append((left, right))
    for a in ans:
        print(*a)

=======
Suggestion 8

def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    X = []
    Y = []
    for i in range(N):
        if len(X) == 0:
            X.append(LR[i][0])
            Y.append(LR[i][1])
        else:
            if LR[i][0] <= Y[-1]:
                Y[-1] = max(LR[i][1], Y[-1])
            else:
                X.append(LR[i][0])
                Y.append(LR[i][1])
    for i in range(len(X)):
        print(X[i], Y[i])

=======
Suggestion 9

def solve():
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    a.sort()
    ans = []
    for i in range(N):
        if i == 0:
            ans.append(a[i])
        else:
            if ans[-1][1] >= a[i][0]:
                ans[-1][1] = max(ans[-1][1], a[i][1])
            else:
                ans.append(a[i])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
solve()
