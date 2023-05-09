Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    intervals = []
    for i in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            intervals.append([l, r])
        elif t == 2:
            intervals.append([l, r-1])
        elif t == 3:
            intervals.append([l+1, r])
        elif t == 4:
            intervals.append([l+1, r-1])
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if intervals[i][0] <= intervals[j][0] <= intervals[i][1]:
                ans += 1
            elif intervals[j][0] <= intervals[i][0] <= intervals[j][1]:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    intervals = []
    for i in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            intervals.append([l, r])
        elif t == 2:
            intervals.append([l, r-0.1])
        elif t == 3:
            intervals.append([l+0.1, r])
        else:
            intervals.append([l+0.1, r-0.1])
    intervals.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if intervals[i][1] >= intervals[j][0]:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    tlr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            t1, l1, r1 = tlr[i]
            t2, l2, r2 = tlr[j]
            if t1 == 1:
                if t2 == 1:
                    if l2 <= r1:
                        ans += 1
                elif t2 == 2:
                    if l2 < r1:
                        ans += 1
                elif t2 == 3:
                    if l2 <= r1:
                        ans += 1
                else:
                    if l2 < r1:
                        ans += 1
            elif t1 == 2:
                if t2 == 1:
                    if l2 <= r1:
                        ans += 1
                elif t2 == 2:
                    if l2 < r1:
                        ans += 1
                elif t2 == 3:
                    if l2 <= r1:
                        ans += 1
                else:
                    if l2 < r1:
                        ans += 1
            elif t1 == 3:
                if t2 == 1:
                    if l2 <= r1:
                        ans += 1
                elif t2 == 2:
                    if l2 < r1:
                        ans += 1
                elif t2 == 3:
                    if l2 <= r1:
                        ans += 1
                else:
                    if l2 < r1:
                        ans += 1
            else:
                if t2 == 1:
                    if l2 <= r1:
                        ans += 1
                elif t2 == 2:
                    if l2 < r1:
                        ans += 1
                elif t2 == 3:
                    if l2 <= r1:
                        ans += 1
                else:
                    if l2 < r1:
                        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    tlr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if tlr[i][0] == 1:
                if tlr[j][0] == 1:
                    if tlr[i][1] <= tlr[j][1] and tlr[j][1] <= tlr[i][2]:
                        ans += 1
                    elif tlr[j][1] <= tlr[i][1] and tlr[i][1] <= tlr[j][2]:
                        ans += 1
                elif tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] and tlr[j][1] < tlr[i][2]:
                        ans += 1
                elif tlr[j][0] == 3:
                    if tlr[i][1] < tlr[j][2] and tlr[j][2] <= tlr[i][2]:
                        ans += 1
                elif tlr[j][0] == 4:
                    if tlr[i][1] < tlr[j][2] and tlr[j][2] < tlr[i][2]:
                        ans += 1
            elif tlr[i][0] == 2:
                if tlr[j][0] == 1:
                    if tlr[i][1] < tlr[j][2] and tlr[j][2] <= tlr[i][2]:
                        ans += 1
                elif tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][1] and tlr[j][1] < tlr[i][2]:
                        ans += 1
                elif tlr[j][0] == 3:
                    if tlr[i][1] < tlr[j][2] and tlr[j][2] <= tlr[i][2]:
                        ans += 1
                elif tlr[j][0] == 4:
                    if tlr[i][1] < tlr[j][2] and tlr[j][2] < tlr[i][2]:
                        ans += 1
            elif tlr[i][0] == 3:
                if

=======
Suggestion 5

def solve():
    N = int(input())
    intervals = []
    for _ in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            intervals.append((l, r))
        elif t == 2:
            intervals.append((l, r - 0.1))
        elif t == 3:
            intervals.append((l + 0.1, r))
        else:
            intervals.append((l + 0.1, r - 0.1))
    intervals.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if intervals[j][0] <= intervals[i][1]:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    tlr = []
    for i in range(N):
        tlr.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if tlr[i][0] == 1:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] and tlr[j][1] <= tlr[i][2]:
                        count += 1
                elif tlr[j][0] == 3 or tlr[j][0] == 4:
                    if tlr[i][1] <= tlr[j][1] and tlr[j][1] < tlr[i][2]:
                        count += 1
            elif tlr[i][0] == 2:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][1] and tlr[j][1] <= tlr[i][2]:
                        count += 1
                elif tlr[j][0] == 3 or tlr[j][0] == 4:
                    if tlr[i][1] < tlr[j][1] and tlr[j][1] < tlr[i][2]:
                        count += 1
            elif tlr[i][0] == 3:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][1] and tlr[j][1] <= tlr[i][2]:
                        count += 1
                elif tlr[j][0] == 3 or tlr[j][0] == 4:
                    if tlr[i][1] < tlr[j][1] and tlr[j][1] < tlr[i][2]:
                        count += 1
            elif tlr[i][0] == 4:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][1] and tlr[j][1] <= tlr[i][2]:
                        count +=

=======
Suggestion 7

def main():
    N = int(input())
    intervals = []
    for i in range(N):
        t, l, r = map(int, input().split())
        intervals.append((t, l, r))
    intervals.sort(key=lambda x: x[1])
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if intervals[i][2] >= intervals[j][1]:
                count += 1
    print(count)

=======
Suggestion 8

def intersect(a, b, c, d):
    if a <= c and c < b:
        return True
    if a < d and d <= b:
        return True
    if c <= a and a < d:
        return True
    if c < b and b <= d:
        return True
    return False

n = int(input())
t = []
l = []
r = []
for i in range(n):
    t_i, l_i, r_i = map(int, input().split())
    t.append(t_i)
    l.append(l_i)
    r.append(r_i)

ans = 0
for i in range(n):
    for j in range(i+1,n):
        if intersect(l[i], r[i], l[j], r[j]) == True:
            ans += 1
print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    for _ in range(n):
        t,l,r = map(int, input().split())
        if t == 2 or t == 4:
            r -= 0.1
        if t == 3 or t == 4:
            l += 0.1
        a.append((l,r))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i][0] <= a[j][1] and a[j][0] <= a[i][1]:
                ans += 1
    print(ans)

=======
Suggestion 10

def check_interval(i,j):
    if t[i] == 1:
        if t[j] == 1:
            if r[i] >= l[j]:
                return True
            else:
                return False
        elif t[j] == 2:
            if r[i] > l[j]:
                return True
            else:
                return False
        elif t[j] == 3:
            if r[i] >= l[j]:
                return True
            else:
                return False
        elif t[j] == 4:
            if r[i] > l[j]:
                return True
            else:
                return False
    elif t[i] == 2:
        if t[j] == 1:
            if r[i] >= l[j]:
                return True
            else:
                return False
        elif t[j] == 2:
            if r[i] > l[j]:
                return True
            else:
                return False
        elif t[j] == 3:
            if r[i] >= l[j]:
                return True
            else:
                return False
        elif t[j] == 4:
            if r[i] > l[j]:
                return True
            else:
                return False
    elif t[i] == 3:
        if t[j] == 1:
            if r[i] > l[j]:
                return True
            else:
                return False
        elif t[j] == 2:
            if r[i] > l[j]:
                return True
            else:
                return False
        elif t[j] == 3:
            if r[i] >= l[j]:
                return True
            else:
                return False
        elif t[j] == 4:
            if r[i] >= l[j]:
                return True
            else:
                return False
    elif t[i] == 4:
        if t[j] == 1:
            if r[i] > l[j]:
                return True
            else:
                return False
        elif t[j] == 2:
            if r[i] > l[j]:
                return True
            else:
                return False
        elif t[j] == 3:
            if r[i] >= l[j]:
                return True
            else:
                return False
        elif t[j] == 4:
            if r[i] >= l[j]:
                return True
            else
