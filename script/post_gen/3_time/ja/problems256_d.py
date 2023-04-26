Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    print(L[0], R[-1] + 1)

=======
Suggestion 2

def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    L = LR[0][0]
    R = LR[0][1]
    for i in range(1, N):
        if LR[i][0] <= R:
            R = max(R, LR[i][1])
        else:
            print(L, R)
            L = LR[i][0]
            R = LR[i][1]
    print(L, R)

=======
Suggestion 3

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort()
    left = l[0][0]
    right = l[0][1]
    for i in range(1, n):
        if l[i][0] <= right:
            right = max(right, l[i][1])
        else:
            print(left, right)
            left = l[i][0]
            right = l[i][1]
    print(left, right)

=======
Suggestion 4

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort()
    ans = []
    ans.append(l[0])
    for i in range(1,n):
        if ans[-1][1] >= l[i][0]:
            ans[-1][1] = max(ans[-1][1],l[i][1])
        else:
            ans.append(l[i])
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1])

=======
Suggestion 5

def main():
    n = int(input())
    lrs = [list(map(int, input().split())) for _ in range(n)]
    lrs.sort()
    l, r = lrs[0]
    for i in range(1, n):
        if r < lrs[i][0]:
            print(l, r)
            l, r = lrs[i]
        else:
            r = max(r, lrs[i][1])
    print(l, r)

=======
Suggestion 6

def main():
    n = int(input())
    lr = [list(map(int, input().split())) for _ in range(n)]
    lr.sort(key=lambda x:x[0])
    l, r = lr[0][0], lr[0][1]
    for i in range(1, n):
        if lr[i][0] <= r:
            r = max(r, lr[i][1])
        else:
            print(l, r)
            l, r = lr[i][0], lr[i][1]
    print(l, r)

=======
Suggestion 7

def main():
    N = int(input())
    LR = []
    for i in range(N):
        L, R = map(int, input().split())
        LR.append([L, R])
    LR.sort()
    ans = []
    ans.append(LR[0])
    for i in range(1, N):
        if ans[-1][1] >= LR[i][0]:
            ans[-1][1] = max(ans[-1][1], LR[i][1])
        else:
            ans.append(LR[i])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

=======
Suggestion 8

def main():
    n = int(input())
    lr = []
    for _ in range(n):
        lr.append(list(map(int,input().split())))
    lr.sort()
    ans = []
    ans.append(lr[0])
    for i in range(1,n):
        if ans[-1][1] >= lr[i][0]:
            ans[-1][1] = max(ans[-1][1],lr[i][1])
        else:
            ans.append(lr[i])
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1])

=======
Suggestion 9

def main():
    N = int(input())
    LR = []
    for _ in range(N):
        L,R = map(int,input().split())
        LR.append((L,R))
    LR.sort()
    ans = []
    L = LR[0][0]
    R = LR[0][1]
    for l,r in LR:
        if l <= R:
            R = max(R,r)
        else:
            ans.append((L,R))
            L = l
            R = r
    ans.append((L,R))
    for l,r in ans:
        print(l,r)

=======
Suggestion 10

def main():
    N = int(input())
    A = []
    for i in range(N):
        L, R = map(int, input().split())
        A.append([L, R])

    A.sort()

    ans = []
    ans.append(A[0])
    for i in range(1, N):
        if A[i][0] < ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], A[i][1])
        else:
            ans.append(A[i])

    for i in ans:
        print(i[0], i[1])
