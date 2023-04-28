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
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if intervals[i][0] <= intervals[j][1] and intervals[j][0] <= intervals[i][1]:
                cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    n = int(input())
    intervals = []
    for i in range(n):
        t, l, r = map(int, input().split())
        if t == 1:
            intervals.append([l, r])
        elif t == 2:
            intervals.append([l, r - 0.1])
        elif t == 3:
            intervals.append([l + 0.1, r])
        elif t == 4:
            intervals.append([l + 0.1, r - 0.1])
    intervals.sort(key=lambda x: x[0])
    #print(intervals)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if intervals[i][1] >= intervals[j][0]:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    intervals = []
    for i in range(N):
        t, l, r = map(int, input().split())
        intervals.append((t, l, r))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if intersect(intervals[i], intervals[j]):
                ans += 1
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    intervals = []
    for i in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            intervals.append((l, r))
        elif t == 2:
            intervals.append((l, r - 0.1))
        elif t == 3:
            intervals.append((l + 0.1, r))
        elif t == 4:
            intervals.append((l + 0.1, r - 0.1))
    intervals.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if intervals[i][1] >= intervals[j][0]:
                ans += 1
    print(ans)
solve()

=======
Suggestion 5

def get_input():
    n = int(input())
    intervals = []
    for i in range(n):
        t, l, r = map(int, input().split())
        intervals.append((t, l, r))
    return intervals

=======
Suggestion 6

def main():
    n = int(input())
    tlr = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
        li, ri = tlr[i][1], tlr[i][2]
        for j in range(i+1, n):
            lj, rj = tlr[j][1], tlr[j][2]
            if (li <= lj and lj <= ri) or (li <= rj and rj <= ri) or (lj <= li and li <= rj) or (lj <= ri and ri <= rj):
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    intervals = []
    for _ in range(N):
        t, l, r = map(int, input().split())
        interval = [l, r]
        if t == 2 or t == 4:
            interval[1] -= 0.1
        if t == 3 or t == 4:
            interval[0] += 0.1
        intervals.append(interval)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if intervals[i][0] <= intervals[j][0] <= intervals[i][1]:
                ans += 1
            elif intervals[i][0] <= intervals[j][1] <= intervals[i][1]:
                ans += 1
            elif intervals[j][0] <= intervals[i][0] <= intervals[j][1]:
                ans += 1
            elif intervals[j][0] <= intervals[i][1] <= intervals[j][1]:
                ans += 1
    print(ans)

=======
Suggestion 8

def func():
    n = int(input())
    intervals = []
    for i in range(n):
        t, l, r = map(int, input().split())
        intervals.append((t, l, r))
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if intervals[i][1] <= intervals[j][1] <= intervals[i][2] or intervals[i][1] <= intervals[j][2] <= intervals[i][2] or intervals[j][1] <= intervals[i][1] <= intervals[j][2] or intervals[j][1] <= intervals[i][2] <= intervals[j][2]:
                count += 1
    print(count)

func()

=======
Suggestion 9

def get_intervals():
    intervals = []
    for i in range(N):
        t, l, r = map(int, input().split())
        intervals.append((t, l, r))
    return intervals

=======
Suggestion 10

def main():
    pass
