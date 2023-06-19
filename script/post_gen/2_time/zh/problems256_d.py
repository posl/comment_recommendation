Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort()
    l = [l[0]] + [l[i] for i in range(1, n) if l[i][0] > l[i-1][1]]
    for i in range(len(l)):
        print(l[i][0], l[i][1])

=======
Suggestion 2

def main():
    n = int(input())
    L = []
    R = []
    for i in range(n):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    ans = 0
    for i in range(n):
        if i == 0 or L[i] > R[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    #S = []
    #for i in range(N):
    #    S.append(input().split())
    #print(S)
    #S.sort(key=lambda x:x[0])
    #print(S)
    #k = 0
    #while k < len(S) - 1:
    #    if S[k][1] >= S[k+1][0]:
    #        S[k][1] = max(S[k][1],S[k+1][1])
    #        del S[k+1]
    #    else:
    #        k += 1
    #for i in range(len(S)):
    #    print(S[i][0],S[i][1])
    #S = []
    #for i in range(N):
    #    S.append(input().split())
    #print(S)
    #S.sort(key=lambda x:x[0])
    #print(S)
    #k = 0
    #while k < len(S) - 1:
    #    if S[k][1] >= S[k+1][0]:
    #        S[k][1] = max(S[k][1],S[k+1][1])
    #        del S[k+1]
    #    else:
    #        k += 1
    #for i in range(len(S)):
    #    print(S[i][0],S[i][1])
    S = []
    for i in range(N):
        S.append(input().split())
    S.sort(key=lambda x:x[0])
    k = 0
    while k < len(S) - 1:
        if S[k][1] >= S[k+1][0]:
            S[k][1] = max(S[k][1],S[k+1][1])
            del S[k+1]
        else:
            k += 1
    for i in range(len(S)):
        print(S[i][0],S[i][1])

=======
Suggestion 4

def main():
    n = int(input())
    lr = []
    for i in range(n):
        lr.append(list(map(int, input().split())))
    lr.sort()

    minL = lr[0][0]
    maxR = lr[0][1]
    for i in range(1, n):
        if lr[i][0] <= maxR:
            maxR = max(maxR, lr[i][1])
        else:
            print(minL, maxR)
            minL = lr[i][0]
            maxR = lr[i][1]
    print(minL, maxR)

=======
Suggestion 5

def main():
    n = int(input())
    L = []
    R = []
    for i in range(n):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    print(L[0],R[-1])
    return 0

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
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))

    l.sort(key=lambda x: x[0])
    result = []
    result.append(l[0])
    for i in range(1, n):
        if result[-1][1] < l[i][0]:
            result.append(l[i])
        else:
            result[-1][1] = max(result[-1][1], l[i][1])

    for i in range(len(result)):
        print(result[i][0], result[i][1])

=======
Suggestion 8

def merge_intervals(intervals):
    intervals.sort()
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

n = int(input())
intervals = []
for i in range(n):
    intervals.append(list(map(int, input().split())))

merged = merge_intervals(intervals)

for interval in merged:
    print(interval[0], interval[1])

=======
Suggestion 9

def main():
    n = int(input())
    lr = []
    for i in range(n):
        l, r = map(int, input().split())
        lr.append([l, r])
    lr.sort()
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
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

main()

=======
Suggestion 10

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

    ans = 0
    for i in range(n):
        if i == 0 or l[i] > r[i-1]:
            ans += 1
    
    print(ans)
