Synthesizing 10/10 solutions

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
    print(L[0], R[-1])

=======
Suggestion 2

def main():
    n = int(input())
    l = []
    r = []
    for i in range(n):
        l_i,r_i = map(int,input().split())
        l.append(l_i)
        r.append(r_i)
    l.sort()
    r.sort()
    print(str(l[0])+" "+str(r[n-1]))

=======
Suggestion 3

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort()
    minl = l[0][0]
    maxr = l[0][1]
    for i in range(1,n):
        if l[i][0] <= maxr:
            maxr = max(maxr,l[i][1])
        else:
            print(minl,maxr)
            minl = l[i][0]
            maxr = l[i][1]
    print(minl,maxr)

=======
Suggestion 4

def main():
    # N = int(input())
    # L = []
    # R = []
    # for i in range(N):
    #     l, r = map(int, input().split())
    #     L.append(l)
    #     R.append(r)
    # L.sort()
    # R.sort()
    # print(L[0], R[-1])
    N = int(input())
    L, R = [], []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    print(L[0], R[-1])

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    for i in range(n):
        l, r = map(int, input().split())
        a.append((l, r))
    a.sort(key=lambda x: x[0])
    ans = []
    for i in range(n):
        if len(ans) == 0:
            ans.append(a[i])
        else:
            if ans[-1][1] >= a[i][0]:
                ans[-1] = (ans[-1][0], max(ans[-1][1], a[i][1]))
            else:
                ans.append(a[i])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

=======
Suggestion 6

def main():
    n = int(input())
    l = []
    r = []
    for i in range(n):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    l.sort()
    r.sort()
    print(l[0], r[n-1]+1)

=======
Suggestion 7

def main():
    n = int(input())
    l = [0]*n
    r = [0]*n
    for i in range(n):
        l[i],r[i] = map(int,input().split())
    l.sort()
    r.sort()
    print(l[0],r[-1]+1)

=======
Suggestion 8

def main():
    n = int(input())
    lr = []
    for _ in range(n):
        l, r = map(int, input().split())
        lr.append((l, r))
    lr.sort()
    l, r = lr[0]
    for i in range(1, n):
        if lr[i][0] <= r:
            r = max(r, lr[i][1])
        else:
            print(l, r)
            l, r = lr[i]
    print(l, r)

=======
Suggestion 9

def main():
    n = int(input())
    lr = [list(map(int, input().split())) for _ in range(n)]
    lr.sort()
    ans = []
    l = lr[0][0]
    r = lr[0][1]
    for i in range(1, n):
        if r < lr[i][0]:
            ans.append([l, r])
            l = lr[i][0]
            r = lr[i][1]
        else:
            r = max(r, lr[i][1])
    ans.append([l, r])
    for a in ans:
        print(a[0], a[1])

=======
Suggestion 10

def main():
    n = int(input())
    lr = [list(map(int, input().split())) for _ in range(n)]
    lr.sort()
    left = lr[0][0]
    right = lr[0][1]
    for i in range(1, n):
        if right < lr[i][0]:
            print(left, right)
            left = lr[i][0]
            right = lr[i][1]
        else:
            if right < lr[i][1]:
                right = lr[i][1]
    print(left, right)
