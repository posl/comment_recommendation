Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    intervals = []
    for i in range(N):
        L, R = map(int, input().split())
        intervals.append((L, R))
    intervals.sort(key=lambda x: x[0])
    ans = []
    for L, R in intervals:
        if not ans or ans[-1][1] < L:
            ans.append((L, R))
        else:
            ans[-1] = (ans[-1][0], max(ans[-1][1], R))
    for L, R in ans:
        print(L, R)

=======
Suggestion 2

def main():
    N = int(input())
    intervals = []
    for _ in range(N):
        L, R = map(int, input().split())
        intervals.append((L, R))
    intervals.sort()
    ans = []
    L, R = intervals[0]
    for l, r in intervals:
        if R < l:
            ans.append((L, R))
            L, R = l, r
        else:
            R = max(R, r)
    ans.append((L, R))
    print(len(ans))
    for L, R in ans:
        print(L, R)

=======
Suggestion 3

def main():
    N = int(input())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i],R[i] = map(int,input().split())
    S = sorted(zip(L,R))
    ans = []
    now = S[0]
    for i in range(1,N):
        if now[1] >= S[i][0]:
            now = (now[0],max(now[1],S[i][1]))
        else:
            ans.append(now)
            now = S[i]
    ans.append(now)
    for i in ans:
        print(i[0],i[1])

=======
Suggestion 4

def main():
    N = int(input())
    R = []
    for i in range(N):
        L, R = map(int, input().split())
        R.append((L, R))
    R.sort(key=lambda x: x[0])
    r = []
    for i in range(N):
        if r == []:
            r.append(R[i])
        else:
            if r[-1][1] < R[i][0]:
                r.append(R[i])
            else:
                r[-1] = (r[-1][0], max(r[-1][1], R[i][1]))
    for i in range(len(r)):
        print(r[i][0], r[i][1])

=======
Suggestion 5

def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort()
    ans = []
    for l, r in LR:
        if not ans or ans[-1][1] < l:
            ans.append([l, r])
        else:
            ans[-1][1] = max(ans[-1][1], r)
    for l, r in ans:
        print(l, r)

=======
Suggestion 6

def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    ans = []
    for L, R in LR:
        if ans:
            if ans[-1][1] >= R:
                continue
            elif ans[-1][1] >= L:
                ans[-1][1] = R
            else:
                ans.append([L, R])
        else:
            ans.append([L, R])
    for a in ans:
        print(*a)

=======
Suggestion 7

def main():
    N = int(input())
    intervals = []
    for i in range(N):
        intervals.append(list(map(int, input().split())))
    intervals.sort()
    ans = []
    for i in range(N):
        if ans == []:
            ans.append(intervals[i])
        else:
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
    for a in ans:
        print(a[0], a[1])

=======
Suggestion 8

def main():
    n = int(input())
    intervals = []
    for _ in range(n):
        intervals.append([int(x) for x in input().split()])
    intervals.sort()
    ans = []
    for i in range(n):
        if len(ans) == 0:
            ans.append(intervals[i])
            continue
        if ans[-1][1] < intervals[i][0]:
            ans.append(intervals[i])
        else:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

=======
Suggestion 9

def main():
    N = int(input())
    A = []
    for _ in range(N):
        s, t = map(int, input().split())
        A.append((s, t))
    A.sort()
    ans = []
    l, r = A[0]
    for s, t in A[1:]:
        if r < s:
            ans.append((l, r))
            l, r = s, t
        else:
            r = max(r, t)
    ans.append((l, r))
    for l, r in ans:
        print(l, r)

=======
Suggestion 10

def main():
    N = int(input())
    LR = []
    for i in range(N):
        LR.append(list(map(int,input().split())))
    LR.sort()
    k = 1
    X = [LR[0][0]]
    Y = [LR[0][1]]
    for i in range(1,N):
        if Y[k-1] >= LR[i][0]:
            if Y[k-1] < LR[i][1]:
                Y[k-1] = LR[i][1]
        else:
            k += 1
            X.append(LR[i][0])
            Y.append(LR[i][1])
    for i in range(k):
        print(X[i],Y[i])
