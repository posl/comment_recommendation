Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    tlr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if tlr[i][0] == 1:
                if tlr[j][0] == 1:
                    if tlr[i][1] <= tlr[j][1] < tlr[i][2]:
                        ans += 1
                    elif tlr[j][1] <= tlr[i][1] < tlr[j][2]:
                        ans += 1
                elif tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] < tlr[i][2]:
                        ans += 1
                elif tlr[j][0] == 3:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2]:
                        ans += 1
                elif tlr[j][0] == 4:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2]:
                        ans += 1
            elif tlr[i][0] == 2:
                if tlr[j][0] == 1:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2]:
                        ans += 1
                    elif tlr[j][1] < tlr[i][1] <= tlr[j][2]:
                        ans += 1
                elif tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2]:
                        ans += 1
                elif tlr[j][0] == 3:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2]:
                        ans += 1
                elif tlr[j][0] == 4:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2]:
                        ans += 1
            elif tlr[i][0] == 3:
                if tlr[j][0] == 1:
                    if tlr[i][1] <= tlr[j][1] < tlr[i][2]:
                        ans +=

=======
Suggestion 2

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i][0] == 1:
                l1 = A[i][1]
            elif A[i][0] == 2:
                l1 = A[i][1] + 1
            elif A[i][0] == 3:
                l1 = A[i][1]
            else:
                l1 = A[i][1] + 1
            if A[j][0] == 1:
                l2 = A[j][1]
            elif A[j][0] == 2:
                l2 = A[j][1] + 1
            elif A[j][0] == 3:
                l2 = A[j][1]
            else:
                l2 = A[j][1] + 1
            if A[i][0] == 1:
                r1 = A[i][2]
            elif A[i][0] == 2:
                r1 = A[i][2]
            elif A[i][0] == 3:
                r1 = A[i][2] - 1
            else:
                r1 = A[i][2] - 1
            if A[j][0] == 1:
                r2 = A[j][2]
            elif A[j][0] == 2:
                r2 = A[j][2]
            elif A[j][0] == 3:
                r2 = A[j][2] - 1
            else:
                r2 = A[j][2] - 1
            if l1 <= l2 <= r1 or l1 <= r2 <= r1 or l2 <= l1 <= r2 or l2 <= r1 <= r2:
                ans += 1
    print(ans)

=======
Suggestion 3

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
                    if l[i] <= l[j] <= r[i] or l[j] <= l[i] <= r[j]:
                        ans += 1
                elif t[j] == 2:
                    if l[i] <= l[j] <= r[i] or l[j] < l[i] <= r[j]:
                        ans += 1
                elif t[j] == 3:
                    if l[i] <= l[j] < r[i] or l[j] <= l[i] < r[j]:
                        ans += 1
                else:
                    if l[i] <= l[j] < r[i] or l[j] < l[i] < r[j]:
                        ans += 1
            elif t[i] == 2:
                if t[j] == 1:
                    if l[i] < l[j] <= r[i] or l[j] <= l[i] < r[j]:
                        ans += 1
                elif t[j] == 2:
                    if l[i] < l[j] <= r[i] or l[j] < l[i] < r[j]:
                        ans += 1
                elif t[j] == 3:
                    if l[i] < l[j] < r[i] or l[j] < l[i] < r[j]:
                        ans += 1
                else:
                    if l[i] < l[j] < r[i] or l[j] < l[i] < r[j]:
                        ans += 1
            elif t[i] == 3:
                if t[j] == 1:
                    if l[i] < l[j] <= r[i] or l[j] <= l[i] < r[j]:
                        ans += 1
                elif t[j] == 2:
                    if l[i] < l[j] < r[i] or l[j] < l[i] < r[j]:
                        ans += 1
                elif t

=======
Suggestion 4

def main():
    N = int(input())
    ranges = []
    for _ in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            ranges.append((l, r))
        elif t == 2:
            ranges.append((l, r - 1))
        elif t == 3:
            ranges.append((l + 1, r))
        else:
            ranges.append((l + 1, r - 1))

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if ranges[i][0] <= ranges[j][1] and ranges[j][0] <= ranges[i][1]:
                ans += 1
    print(ans)

=======
Suggestion 5

def solve():
    N = int(input())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            L[i] = l
            R[i] = r
        elif t == 2:
            L[i] = l
            R[i] = r - 1
        elif t == 3:
            L[i] = l + 1
            R[i] = r
        else:
            L[i] = l + 1
            R[i] = r - 1
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if L[i] <= R[j] and L[j] <= R[i]:
                cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    n = int(input())
    tlr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if tlr[i][0] == 1:
                if tlr[j][0] == 1:
                    if tlr[i][1] <= tlr[j][1] <= tlr[i][2]:
                        cnt += 1
                    elif tlr[j][1] <= tlr[i][1] <= tlr[j][2]:
                        cnt += 1
                elif tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] < tlr[i][2]:
                        cnt += 1
                    elif tlr[j][1] < tlr[i][1] <= tlr[j][2]:
                        cnt += 1
                elif tlr[j][0] == 3:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2]:
                        cnt += 1
                    elif tlr[j][1] <= tlr[i][1] < tlr[j][2]:
                        cnt += 1
                else:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2]:
                        cnt += 1
                    elif tlr[j][1] < tlr[i][1] < tlr[j][2]:
                        cnt += 1
            elif tlr[i][0] == 2:
                if tlr[j][0] == 1:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2]:
                        cnt += 1
                    elif tlr[j][1] <= tlr[i][1] < tlr[j][2]:
                        cnt += 1
                elif tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2]:
                        cnt += 1
                    elif tlr[j][1] < tlr[i][1] < tlr[j][2]:
                        cnt += 1
                elif tlr[j][0] == 3:
                    if tlr[i][1] < tlr[j][1

=======
Suggestion 7

def main():
    N = int(input())
    l = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if l[i][0] == 1:
                if l[j][0] == 1:
                    if l[i][1] <= l[j][1] <= l[i][2]:
                        ans += 1
                    if l[i][1] <= l[j][2] <= l[i][2]:
                        ans += 1
                elif l[j][0] == 2:
                    if l[i][1] <= l[j][1] <= l[i][2]:
                        ans += 1
                elif l[j][0] == 3:
                    if l[i][1] <= l[j][2] <= l[i][2]:
                        ans += 1
                elif l[j][0] == 4:
                    if l[i][1] <= l[j][1] <= l[i][2]:
                        ans += 1
                    if l[i][1] <= l[j][2] <= l[i][2]:
                        ans += 1
            elif l[i][0] == 2:
                if l[j][0] == 1:
                    if l[i][1] <= l[j][1] <= l[i][2]:
                        ans += 1
                elif l[j][0] == 2:
                    if l[i][1] < l[j][1] < l[i][2]:
                        ans += 1
                    if l[i][1] < l[j][2] < l[i][2]:
                        ans += 1
                elif l[j][0] == 3:
                    if l[i][1] < l[j][2] < l[i][2]:
                        ans += 1
                elif l[j][0] == 4:
                    if l[i][1] < l[j][1] < l[i][2]:
                        ans += 1
                    if l[i][1] < l[j][2] < l[i][2]:
                        ans += 1
            elif l[i][0] == 3:
                if l[j][0] == 1:
                    if l[i][1] <= l[j][2] <= l[i][2

=======
Suggestion 8

def main():
    import sys
    from bisect import bisect_left, bisect_right
    readline = sys.stdin.readline
    N = int(readline())
    L = []
    R = []
    for _ in range(N):
        t, l, r = map(int, readline().split())
        if t == 1:
            L.append(l)
            R.append(r)
        elif t == 2:
            L.append(l)
            R.append(r - 1)
        elif t == 3:
            L.append(l + 1)
            R.append(r)
        else:
            L.append(l + 1)
            R.append(r - 1)
    L.sort()
    R.sort()
    ans = 0
    for i in range(N):
        l = bisect_left(R, L[i])
        r = bisect_right(L, R[i])
        ans += r - l
    print(ans)

main()

=======
Suggestion 9

def main():
    N = int(input())
    # 1,2,3,4のリストを作成
    t = [0] * N
    l = [0] * N
    r = [0] * N
    for i in range(N):
        t[i], l[i], r[i] = map(int, input().split())
    # 重複を排除した区間のリストを作成
    interval = []
    for i in range(N):
        if t[i] == 1:
            interval.append((l[i], r[i]))
        elif t[i] == 2:
            interval.append((l[i], r[i] - 1))
        elif t[i] == 3:
            interval.append((l[i] + 1, r[i]))
        else:
            interval.append((l[i] + 1, r[i] - 1))
    # 重複を排除した区間のリストをソート
    interval.sort()
    # 重複を排除した区間のリストの要素を順番に取り出す
    ans = 0
    for i in range(N):
        # 取り出した要素をtmpとする
        tmp = interval[i]
        # tmpの右端より小さい区間のリストを作成
        tmp_list = []
        for j in range(N):
            if interval[j][1] < tmp[1]:
                tmp_list.append(interval[j])
        # tmp_listの要素を順番に取り出す
        for j in range(len(tmp_list)):
            # 取り出した要素をtmp2とする
            tmp2 = tmp_list[j]
            # tmpの左端がtmp2の左端より小さいかつtmpの左端がtmp2の右端より小さいか
            if tmp[0] > tmp2[0] and tmp[0] < tmp2[1]:
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    # 区間の左端と右端をそれぞれリストに格納
    lefts = [0] * N
    rights = [0] * N
    for i in range(N):
        t, l, r = map(int, input().split())
        # 区間の左端と右端をそれぞれリストに格納
        lefts[i] = l
        rights[i] = r
        # 区間の左端と右端をそれぞれリストに格納
        if t == 1:
            lefts[i] = l
            rights[i] = r
        elif t == 2:
            lefts[i] = l
            rights[i] = r - 1
        elif t == 3:
            lefts[i] = l + 1
            rights[i] = r
        elif t == 4:
            lefts[i] = l + 1
            rights[i] = r - 1

    # 区間の左端と右端のリストから、共通部分を持つ区間の組み合わせをカウント
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if lefts[i] <= rights[j] and lefts[j] <= rights[i]:
                count += 1

    print(count)
