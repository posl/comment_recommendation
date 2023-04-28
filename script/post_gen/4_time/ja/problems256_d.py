Synthesizing 10/10 solutions (Duplicates hidden)

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
    N = int(input())
    Ls = []
    Rs = []
    for _ in range(N):
        L, R = map(int, input().split())
        Ls.append(L)
        Rs.append(R)
    Ls.sort()
    Rs.sort()
    L = Ls[0]
    R = Rs[-1]
    print(L, R+1)

=======
Suggestion 3

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
    print(l[0], r[-1])

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
    for i in range(1, n):
        if ans[-1][1] >= l[i][0]:
            ans[-1][1] = max(ans[-1][1], l[i][1])
        else:
            ans.append(l[i])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

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
        if l[i][0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1],l[i][1])
        else:
            ans.append(l[i])
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1])

=======
Suggestion 6

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort()
    ans = []
    left = l[0][0]
    right = l[0][1]
    for i in range(1,n):
        if right < l[i][0]:
            ans.append([left,right])
            left = l[i][0]
            right = l[i][1]
        elif right < l[i][1]:
            right = l[i][1]
    ans.append([left,right])
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1])

=======
Suggestion 7

def main():
    n = int(input())
    lr = []
    for i in range(n):
        lr.append(list(map(int, input().split())))
    lr.sort()

    ans = []
    ans.append(lr[0])
    for i in range(1, n):
        if ans[-1][1] >= lr[i][0]:
            ans[-1][1] = max(ans[-1][1], lr[i][1])
        else:
            ans.append(lr[i])

    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

=======
Suggestion 8

def solve():
    n = int(input())
    lr = [list(map(int, input().split())) for _ in range(n)]
    lr.sort(key=lambda x: x[0])
    ans = []
    ans.append([lr[0][0], lr[0][1]])
    for i in range(1, n):
        if ans[-1][1] < lr[i][0]:
            ans.append([lr[i][0], lr[i][1]])
        else:
            if ans[-1][1] < lr[i][1]:
                ans[-1][1] = lr[i][1]
    for i in range(len(ans)):
        print(*ans[i])

solve()

=======
Suggestion 9

def main():
    N = int(input())

    d = {}
    for i in range(N):
        L, R = map(int, input().split())
        if L in d:
            if R in d:
                if d[L] > d[R]:
                    d[L] = d[R]
                else:
                    d[R] = d[L]
            else:
                d[R] = d[L]
        else:
            if R in d:
                d[L] = d[R]
            else:
                d[L] = L
                d[R] = L
    
    d = sorted(d.items())
    #print(d)
    ans = []
    i = 0
    while i < len(d):
        if i == len(d) - 1:
            ans.append(d[i][1])
            break
        if d[i][1] == d[i+1][1]:
            ans.append(d[i][1])
            i += 1
        else:
            ans.append(d[i][1])
        i += 1
    #print(ans)
    for i in range(0, len(ans), 2):
        print(ans[i], ans[i+1])
