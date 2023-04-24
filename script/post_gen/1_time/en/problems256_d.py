Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    intervals = []
    for _ in range(N):
        L, R = map(int, input().split())
        intervals.append((L, R))
    intervals.sort(key=lambda x: x[0])
    ans = []
    L, R = intervals[0]
    for i in range(1, N):
        if R < intervals[i][0]:
            ans.append((L, R))
            L, R = intervals[i]
        else:
            R = max(R, intervals[i][1])
    ans.append((L, R))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

=======
Suggestion 2

def main():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)

    L.sort()
    R.sort()

    ans = []
    l = L[0]
    r = R[0]
    for i in range(N-1):
        if l <= L[i+1] and R[i+1] <= r:
            continue
        elif l <= L[i+1] and L[i+1] <= r:
            r = R[i+1]
        else:
            ans.append([l,r])
            l = L[i+1]
            r = R[i+1]
    ans.append([l,r])

    for a in ans:
        print(*a)

=======
Suggestion 3

def main():
    N = int(input())
    intervals = []
    for i in range(N):
        L, R = map(int, input().split())
        intervals.append((L, R))
    intervals.sort()
    ans = []
    L, R = intervals[0]
    for i in range(1,N):
        if R < intervals[i][0]:
            ans.append((L, R))
            L, R = intervals[i]
        else:
            R = max(R, intervals[i][1])
    ans.append((L, R))
    for i in ans:
        print(i[0], i[1])

=======
Suggestion 4

def get_input():
    N = int(input())
    intervals = []
    for _ in range(N):
        L, R = map(int, input().split())
        intervals.append((L, R))
    return N, intervals

=======
Suggestion 5

def solve():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort()
    ans = [[A[0][0], A[0][1]]]
    for i in range(1, N):
        if ans[-1][1] < A[i][0]:
            ans.append([A[i][0], A[i][1]])
        else:
            ans[-1][1] = max(ans[-1][1], A[i][1])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
    return 0

=======
Suggestion 6

def main():
    N = int(input())
    intervals = []
    for i in range(N):
        L, R = map(int, input().split())
        intervals.append([L, R])
    intervals.sort()

    L, R = intervals[0]
    for i in range(1, N):
        if R < intervals[i][0]:
            print(L, R)
            L, R = intervals[i]
        else:
            R = max(R, intervals[i][1])
    print(L, R)

main()

=======
Suggestion 7

def main():
    N = int(input())
    LR = []
    for i in range(N):
        LR.append(list(map(int, input().split())))
    LR.sort(key=lambda x: x[0])
    ans = []
    ans.append(LR[0])
    for i in range(1, N):
        if ans[-1][1] >= LR[i][1]:
            continue
        elif ans[-1][1] >= LR[i][0]:
            ans[-1][1] = LR[i][1]
        else:
            ans.append(LR[i])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

=======
Suggestion 8

def main():
    N = int(input())
    intervals = [list(map(int, input().split())) for _ in range(N)]
    intervals.sort()
    ans = []
    for i in range(N):
        if i == 0:
            ans.append(intervals[i])
        else:
            if ans[-1][1] >= intervals[i][1]:
                continue
            elif ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = intervals[i][1]
            else:
                ans.append(intervals[i])
    for a in ans:
        print(*a)

=======
Suggestion 9

def main():
    n = int(input())
    l = [tuple(map(int, input().split())) for _ in range(n)]
    l.sort()
    r = []
    for a in l:
        if r and r[-1][1] >= a[1]:
            continue
        if r and r[-1][1] >= a[0]:
            r[-1] = (r[-1][0], a[1])
        else:
            r.append(a)
    for a in r:
        print(*a)

=======
Suggestion 10

def readInt():
    return int(input())
