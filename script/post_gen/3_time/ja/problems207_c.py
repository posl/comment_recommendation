Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            L.append(l)
            R.append(r)
        elif t == 2:
            L.append(l)
            R.append(r-0.1)
        elif t == 3:
            L.append(l+0.1)
            R.append(r)
        elif t == 4:
            L.append(l+0.1)
            R.append(r-0.1)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if L[i] <= R[j] and R[i] >= L[j]:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    L = []
    R = []
    for _ in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            L.append(l)
            R.append(r)
        elif t == 2:
            L.append(l)
            R.append(r-0.5)
        elif t == 3:
            L.append(l+0.5)
            R.append(r)
        elif t == 4:
            L.append(l+0.5)
            R.append(r-0.5)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if L[i] <= R[j] and L[j] <= R[i]:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    tlr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += not (tlr[j][1] <= tlr[i][1] and tlr[i][2] <= tlr[j][2]) and \
                not (tlr[j][1] >= tlr[i][2] or tlr[i][1] >= tlr[j][2]) and \
                not (tlr[j][1] == tlr[i][1] and tlr[i][2] == tlr[j][2] and tlr[i][0] == 1 and tlr[j][0] == 1) and \
                not (tlr[j][1] == tlr[i][1] and tlr[i][2] == tlr[j][2] and tlr[i][0] == 2 and tlr[j][0] == 2) and \
                not (tlr[j][1] == tlr[i][1] and tlr[i][2] == tlr[j][2] and tlr[i][0] == 3 and tlr[j][0] == 3) and \
                not (tlr[j][1] == tlr[i][1] and tlr[i][2] == tlr[j][2] and tlr[i][0] == 4 and tlr[j][0] == 4)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if data[i][0] == 1:
                l = data[i][1]
            else:
                l = data[i][1]+1
            if data[i][0] == 3:
                r = data[i][2]
            else:
                r = data[i][2]-1
            if data[j][0] == 1:
                l2 = data[j][1]
            else:
                l2 = data[j][1]+1
            if data[j][0] == 3:
                r2 = data[j][2]
            else:
                r2 = data[j][2]-1
            if l <= r2 and l2 <= r:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    T = [0] * N
    L = [0] * N
    R = [0] * N
    ans = 0
    for i in range(N):
        T[i], L[i], R[i] = map(int, input().split())
        if T[i] == 1:
            L[i] *= 2
            R[i] = R[i] * 2 - 1
        elif T[i] == 2:
            L[i] *= 2
            R[i] = R[i] * 2 - 2
        elif T[i] == 3:
            L[i] = L[i] * 2 + 1
            R[i] = R[i] * 2
        else:
            L[i] = L[i] * 2 + 2
            R[i] = R[i] * 2
    for i in range(N):
        for j in range(i + 1, N):
            if max(L[i], L[j]) <= min(R[i], R[j]):
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    for _ in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            S.append((l, r))
        elif t == 2:
            S.append((l, r - 1))
        elif t == 3:
            S.append((l + 1, r))
        else:
            S.append((l + 1, r - 1))
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if S[i][0] <= S[j][1] and S[j][0] <= S[i][1]:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    L = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if L[i][0] == 1:
                if L[j][0] == 1:
                    if L[i][1] <= L[j][1] <= L[i][2]:
                        ans += 1
                    if L[j][1] <= L[i][1] <= L[j][2]:
                        ans += 1
                if L[j][0] == 2:
                    if L[i][1] <= L[j][1] <= L[i][2]:
                        ans += 1
                    if L[j][1] <= L[i][1] < L[j][2]:
                        ans += 1
                if L[j][0] == 3:
                    if L[i][1] < L[j][1] <= L[i][2]:
                        ans += 1
                    if L[j][1] <= L[i][1] <= L[j][2]:
                        ans += 1
                if L[j][0] == 4:
                    if L[i][1] < L[j][1] < L[i][2]:
                        ans += 1
                    if L[j][1] <= L[i][1] < L[j][2]:
                        ans += 1
            if L[i][0] == 2:
                if L[j][0] == 1:
                    if L[i][1] <= L[j][1] <= L[i][2]:
                        ans += 1
                    if L[j][1] <= L[i][1] < L[j][2]:
                        ans += 1
                if L[j][0] == 2:
                    if L[i][1] <= L[j][1] <= L[i][2]:
                        ans += 1
                    if L[j][1] < L[i][1] <= L[j][2]:
                        ans += 1
                if L[j][0] == 3:
                    if L[i][1] < L[j][1] <= L[i][2]:
                        ans += 1
                    if L[j][1] < L[i][1] <= L[j][2]:
                        ans += 1

=======
Suggestion 8

def main():
    N = int(input())
    li = []
    for i in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            li.append([l, r])
        elif t == 2:
            li.append([l, r - 1])
        elif t == 3:
            li.append([l + 1, r])
        else:
            li.append([l + 1, r - 1])
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if li[i][0] <= li[j][1] and li[j][0] <= li[i][1]:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    tlr = []
    for _ in range(N):
        tlr.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if tlr[i][0] == 1:
                l1 = tlr[i][1]
                r1 = tlr[i][2]
            elif tlr[i][0] == 2:
                l1 = tlr[i][1]
                r1 = tlr[i][2] - 1
            elif tlr[i][0] == 3:
                l1 = tlr[i][1] + 1
                r1 = tlr[i][2]
            elif tlr[i][0] == 4:
                l1 = tlr[i][1] + 1
                r1 = tlr[i][2] - 1
            if tlr[j][0] == 1:
                l2 = tlr[j][1]
                r2 = tlr[j][2]
            elif tlr[j][0] == 2:
                l2 = tlr[j][1]
                r2 = tlr[j][2] - 1
            elif tlr[j][0] == 3:
                l2 = tlr[j][1] + 1
                r2 = tlr[j][2]
            elif tlr[j][0] == 4:
                l2 = tlr[j][1] + 1
                r2 = tlr[j][2] - 1
            if r1 < l2 or r2 < l1:
                continue
            else:
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    # 区間の始点、終点、区間の種類を格納する配列
    intervals = [[0]*4 for i in range(N)]
    for i in range(N):
        intervals[i] = list(map(int, input().split()))
    # 区間の始点、終点、区間の種類をそれぞれ昇順にソートする
    intervals.sort(key=lambda x: (x[1], x[0], x[2]))
    # 区間の種類ごとに、始点と終点のリストを作成する
    intervals_start = [[], [], [], []]
    intervals_end = [[], [], [], []]
    for i in range(N):
        intervals_start[intervals[i][0]-1].append(intervals[i][1])
        intervals_end[intervals[i][0]-1].append(intervals[i][2])
    # 区間の種類ごとに、始点と終点のリストを昇順にソートする
    for i in range(4):
        intervals_start[i].sort()
        intervals_end[i].sort()
    # 重複する区間の個数をカウントする
    cnt = 0
    for i in range(N):
        # 区間の種類を取り出す
        t = intervals[i][0]
        # 区間の終点を取り出す
        r = intervals[i][2]
        # 区間の種類が1,2の場合
        if t == 1 or t == 2:
            # 区間の終点より大きい始点の個数をカウントする
            cnt += len(intervals_start[0]) - bisect.bisect_left(intervals_start[0], r)
            cnt += len(intervals_start[1]) - bisect.bisect_left(intervals_start[1], r)
            # 区間の終点より大きい終点の個数をカウントする
            cnt += len(intervals_end[2]) - bisect.bisect
