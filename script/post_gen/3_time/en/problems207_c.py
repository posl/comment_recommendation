Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T = []
    L = []
    R = []
    for i in range(N):
        t, l, r = map(int, input().split())
        T.append(t)
        L.append(l)
        R.append(r)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if (T[i] == 1 or T[i] == 2) and (T[j] == 1 or T[j] == 3):
                if L[i] <= L[j] and L[j] < R[i]:
                    ans += 1
            elif (T[i] == 1 or T[i] == 2) and (T[j] == 2 or T[j] == 4):
                if L[i] <= L[j] and L[j] <= R[i]:
                    ans += 1
            elif (T[i] == 3 or T[i] == 4) and (T[j] == 1 or T[j] == 3):
                if L[i] < L[j] and L[j] < R[i]:
                    ans += 1
            elif (T[i] == 3 or T[i] == 4) and (T[j] == 2 or T[j] == 4):
                if L[i] < L[j] and L[j] <= R[i]:
                    ans += 1
            elif T[i] == 1 and T[j] == 4:
                if L[i] <= L[j] and L[j] <= R[i]:
                    ans += 1
            elif T[i] == 4 and T[j] == 1:
                if L[i] <= L[j] and L[j] <= R[i]:
                    ans += 1
            elif T[i] == 2 and T[j] == 3:
                if L[i] <= L[j] and L[j] <= R[i]:
                    ans += 1
            elif T[i] == 3 and T[j] == 2:
                if L[i] <= L[j] and L[j] <= R[i]:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    T = []
    L = []
    R = []
    for i in range(N):
        t, l, r = map(int, input().split())
        T.append(t)
        L.append(l)
        R.append(r)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if T[i] == 1:
                p = L[i]
            elif T[i] == 2:
                p = L[i] + 1
            elif T[i] == 3:
                p = R[i] - 1
            else:
                p = R[i]
            if T[j] == 1:
                q = L[j]
            elif T[j] == 2:
                q = L[j] + 1
            elif T[j] == 3:
                q = R[j] - 1
            else:
                q = R[j]
            if p <= q:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    t = [0] * N
    l = [0] * N
    r = [0] * N
    for i in range(N):
        t[i], l[i], r[i] = map(int, input().split())

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if t[i] == 1:
                if t[j] == 1:
                    ans += (l[i] <= l[j] <= r[i]) or (l[j] <= l[i] <= r[j])
                elif t[j] == 2:
                    ans += (l[i] <= l[j] < r[i]) or (l[j] < l[i] <= r[j])
                elif t[j] == 3:
                    ans += (l[i] < l[j] <= r[i]) or (l[j] <= l[i] < r[j])
                elif t[j] == 4:
                    ans += (l[i] < l[j] < r[i]) or (l[j] < l[i] < r[j])
            elif t[i] == 2:
                if t[j] == 1:
                    ans += (l[i] < l[j] <= r[i]) or (l[j] <= l[i] < r[j])
                elif t[j] == 2:
                    ans += (l[i] < l[j] < r[i]) or (l[j] < l[i] < r[j])
                elif t[j] == 3:
                    ans += (l[i] < l[j] < r[i]) or (l[j] < l[i] < r[j])
                elif t[j] == 4:
                    ans += (l[i] < l[j] < r[i]) or (l[j] < l[i] < r[j])
            elif t[i] == 3:
                if t[j] == 1:
                    ans += (l[i] <= l[j] < r[i]) or (l[j] < l[i] <= r[j])
                elif t[j] == 2:
                    ans += (l[i] < l[j] < r[i]) or (l[j] < l[i] < r[j])
                elif t[j] == 3:
                    ans += (l[i] < l[j

=======
Suggestion 4

def main():
    N = int(input())
    T, L, R = [], [], []
    for _ in range(N):
        t, l, r = map(int, input().split())
        T.append(t)
        L.append(l)
        R.append(r)

    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if T[i] == 1:
                if T[j] == 1:
                    if L[i] <= L[j] <= R[i] or L[i] <= R[j] <= R[i]:
                        ans += 1
                elif T[j] == 2:
                    if L[i] <= L[j] <= R[i] or L[i] <= R[j] < R[i]:
                        ans += 1
                elif T[j] == 3:
                    if L[i] < L[j] <= R[i] or L[i] < R[j] < R[i]:
                        ans += 1
                else:
                    if L[i] < L[j] <= R[i] or L[i] < R[j] < R[i]:
                        ans += 1
            elif T[i] == 2:
                if T[j] == 1:
                    if L[i] <= L[j] <= R[i] or L[i] < R[j] <= R[i]:
                        ans += 1
                elif T[j] == 2:
                    if L[i] <= L[j] <= R[i] or L[i] < R[j] <= R[i]:
                        ans += 1
                elif T[j] == 3:
                    if L[i] < L[j] <= R[i] or L[i] < R[j] <= R[i]:
                        ans += 1
                else:
                    if L[i] < L[j] <= R[i] or L[i] < R[j] <= R[i]:
                        ans += 1
            elif T[i] == 3:
                if T[j] == 1:
                    if L[i] <= L[j] < R[i] or L[i] <= R[j] < R[i]:
                        ans += 1
                elif T[j] == 2:
                    if L[i] <= L[j] < R[i] or L[i] < R[j] < R[i]:
                        ans += 1
                elif T

=======
Suggestion 5

def main():
    N = int(input())
    intervals = []
    for _ in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            intervals.append((l, r))
        elif t == 2:
            intervals.append((l, r - 1))
        elif t == 3:
            intervals.append((l + 1, r))
        else:
            intervals.append((l + 1, r - 1))
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if intervals[i][0] <= intervals[j][1] and intervals[j][0] <= intervals[i][1]:
                count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    intervals = []
    for _ in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            intervals.append([l, r])
        elif t == 2:
            intervals.append([l, r-1])
        elif t == 3:
            intervals.append([l+1, r])
        else:
            intervals.append([l+1, r-1])
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if intervals[i][1] < intervals[j][0] or intervals[j][1] < intervals[i][0]:
                continue
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    t = []
    l = []
    r = []
    for i in range(n):
        t_i, l_i, r_i = map(int, input().split())
        t.append(t_i)
        l.append(l_i)
        r.append(r_i)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (t[i] == 1 and t[j] == 2) or (t[i] == 2 and t[j] == 1):
                if l[i] <= l[j] and l[j] <= r[i]:
                    count += 1
            elif (t[i] == 1 and t[j] == 3) or (t[i] == 3 and t[j] == 1):
                if l[i] <= l[j] and l[j] < r[i]:
                    count += 1
            elif (t[i] == 1 and t[j] == 4) or (t[i] == 4 and t[j] == 1):
                if l[i] < l[j] and l[j] < r[i]:
                    count += 1
            elif (t[i] == 2 and t[j] == 3) or (t[i] == 3 and t[j] == 2):
                if l[i] < l[j] and l[j] < r[i]:
                    count += 1
            elif (t[i] == 2 and t[j] == 4) or (t[i] == 4 and t[j] == 2):
                if l[i] < l[j] and l[j] <= r[i]:
                    count += 1
            elif (t[i] == 3 and t[j] == 4) or (t[i] == 4 and t[j] == 3):
                if l[i] < l[j] and l[j] < r[i]:
                    count += 1
            else:
                if l[i] <= l[j] and l[j] <= r[i]:
                    count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    t = []
    l = []
    r = []
    for i in range(n):
        t_, l_, r_ = map(int, input().split())
        t.append(t_)
        l.append(l_)
        r.append(r_)

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if t[i] == 1:
                if t[j] == 1:
                    if l[i] <= l[j] <= r[i] or l[i] <= r[j] <= r[i] or l[j] <= l[i] <= r[j] or l[j] <= r[i] <= r[j]:
                        ans += 1
                elif t[j] == 2:
                    if l[i] <= l[j] <= r[i] or l[i] <= r[j] <= r[i] or l[j] < l[i] <= r[j] or l[j] < r[i] <= r[j]:
                        ans += 1
                elif t[j] == 3:
                    if l[i] < l[j] <= r[i] or l[i] < r[j] <= r[i] or l[j] <= l[i] < r[j] or l[j] <= r[i] < r[j]:
                        ans += 1
                else:
                    if l[i] < l[j] <= r[i] or l[i] < r[j] <= r[i] or l[j] < l[i] < r[j] or l[j] < r[i] < r[j]:
                        ans += 1
            elif t[i] == 2:
                if t[j] == 1:
                    if l[i] <= l[j] <= r[i] or l[i] <= r[j] <= r[i] or l[j] <= l[i] <= r[j] or l[j] <= r[i] <= r[j]:
                        ans += 1
                elif t[j] == 2:
                    if l[i] <= l[j] <= r[i] or l[i] <= r[j] <= r[i] or l[j] < l[i] <= r[j] or l[j] < r[i] <= r[j]:
                        ans += 1
                elif t[j] == 3:
                    if l[i] < l[j] <= r[i]

=======
Suggestion 9

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    tlr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if tlr[i][0] == 1 and tlr[j][0] == 1:
                if tlr[i][1] <= tlr[j][1] <= tlr[i][2]:
                    ans += 1
                elif tlr[j][1] <= tlr[i][1] <= tlr[j][2]:
                    ans += 1
            elif tlr[i][0] == 1 and tlr[j][0] == 2:
                if tlr[i][1] <= tlr[j][1] < tlr[i][2]:
                    ans += 1
                elif tlr[j][1] <= tlr[i][1] < tlr[j][2]:
                    ans += 1
            elif tlr[i][0] == 1 and tlr[j][0] == 3:
                if tlr[i][1] < tlr[j][1] <= tlr[i][2]:
                    ans += 1
                elif tlr[j][1] < tlr[i][1] <= tlr[j][2]:
                    ans += 1
            elif tlr[i][0] == 1 and tlr[j][0] == 4:
                if tlr[i][1] < tlr[j][1] < tlr[i][2]:
                    ans += 1
                elif tlr[j][1] < tlr[i][1] < tlr[j][2]:
                    ans += 1
            elif tlr[i][0] == 2 and tlr[j][0] == 1:
                if tlr[i][1] < tlr[j][1] <= tlr[i][2]:
                    ans += 1
                elif tlr[j][1] < tlr[i][1] <= tlr[j][2]:
                    ans += 1
            elif tlr[i][0] == 2 and tlr[j][0] == 2:
                if tlr[i][1] < tlr[j][1] < tlr[i][2]:
                    ans +=

=======
Suggestion 10

def main():
    N = int(input())
    tlr = [list(map(int, input().split())) for _ in range(N)]

    # 1.各区間の左端と右端をそれぞれリストに格納する
    left = []
    right = []
    for t, l, r in tlr:
        if t == 1:
            left.append(l)
            right.append(r)
        elif t == 2:
            left.append(l)
            right.append(r-1)
        elif t == 3:
            left.append(l+1)
            right.append(r)
        else:
            left.append(l+1)
            right.append(r-1)

    # 2.各区間の左端と右端の組み合わせをカウントする
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if left[i] <= right[j] and left[j] <= right[i]:
                ans += 1

    print(ans)
