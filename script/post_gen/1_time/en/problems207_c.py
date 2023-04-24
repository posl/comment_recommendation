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
        for j in range(i+1,N):
            if T[i] == 1:
                if T[j] == 1:
                    if L[i] <= R[j] and L[j] <= R[i]:
                        ans += 1
                elif T[j] == 2:
                    if L[i] < R[j] and L[j] <= R[i]:
                        ans += 1
                elif T[j] == 3:
                    if L[i] <= R[j] and L[j] < R[i]:
                        ans += 1
                elif T[j] == 4:
                    if L[i] < R[j] and L[j] < R[i]:
                        ans += 1
            elif T[i] == 2:
                if T[j] == 1:
                    if L[i] <= R[j] and L[j] < R[i]:
                        ans += 1
                elif T[j] == 2:
                    if L[i] < R[j] and L[j] < R[i]:
                        ans += 1
                elif T[j] == 3:
                    if L[i] <= R[j] and L[j] <= R[i]:
                        ans += 1
                elif T[j] == 4:
                    if L[i] < R[j] and L[j] <= R[i]:
                        ans += 1
            elif T[i] == 3:
                if T[j] == 1:
                    if L[i] < R[j] and L[j] <= R[i]:
                        ans += 1
                elif T[j] == 2:
                    if L[i] <= R[j] and L[j] < R[i]:
                        ans += 1
                elif T[j] == 3:
                    if L[i] < R[j] and L[j] < R[i]:
                        ans += 1
                elif T[j] == 4:
                    if L[i] <= R[j] and L[j] < R[i]:
                        ans += 1
            elif T[i] == 4:

=======
Suggestion 2

def main():
    N = int(input())
    t = [0] * N
    l = [0] * N
    r = [0] * N
    for i in range(N):
        t[i], l[i], r[i] = map(int, input().split())
    #print(N, t, l, r)
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if t[i] == 1 and t[j] == 1:
                if l[i] <= l[j] <= r[i] or l[j] <= l[i] <= r[j]:
                    count += 1
            elif t[i] == 1 and t[j] == 2:
                if l[i] <= l[j] < r[i] or l[j] < l[i] <= r[j]:
                    count += 1
            elif t[i] == 1 and t[j] == 3:
                if l[i] < l[j] <= r[i] or l[j] <= l[i] < r[j]:
                    count += 1
            elif t[i] == 1 and t[j] == 4:
                if l[i] < l[j] < r[i] or l[j] < l[i] < r[j]:
                    count += 1
            elif t[i] == 2 and t[j] == 1:
                if l[i] <= l[j] <= r[i] or l[j] <= l[i] <= r[j]:
                    count += 1
            elif t[i] == 2 and t[j] == 2:
                if l[i] <= l[j] < r[i] or l[j] < l[i] <= r[j]:
                    count += 1
            elif t[i] == 2 and t[j] == 3:
                if l[i] < l[j] <= r[i] or l[j] <= l[i] < r[j]:
                    count += 1
            elif t[i] == 2 and t[j] == 4:
                if l[i] < l[j] < r[i] or l[j] < l[i] < r[j]:
                    count += 1
            elif t[i] == 3 and t[j] == 1:
                if l[i] <= l[j] <= r[i] or

=======
Suggestion 3

def main():
    N = int(input())
    t = []
    l = []
    r = []
    for i in range(N):
        t_i, l_i, r_i = map(int, input().split())
        t.append(t_i)
        l.append(l_i)
        r.append(r_i)
    #print(t)
    #print(l)
    #print(r)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if t[i] == 1 and t[j] == 1:
                if l[i] <= l[j] and l[j] <= r[i]:
                    count += 1
                elif l[j] <= l[i] and l[i] <= r[j]:
                    count += 1
            elif t[i] == 1 and t[j] == 2:
                if l[i] <= l[j] and l[j] < r[i]:
                    count += 1
                elif l[j] < l[i] and l[i] <= r[j]:
                    count += 1
            elif t[i] == 1 and t[j] == 3:
                if l[i] < l[j] and l[j] <= r[i]:
                    count += 1
                elif l[j] <= l[i] and l[i] < r[j]:
                    count += 1
            elif t[i] == 1 and t[j] == 4:
                if l[i] < l[j] and l[j] < r[i]:
                    count += 1
                elif l[j] < l[i] and l[i] < r[j]:
                    count += 1
            elif t[i] == 2 and t[j] == 1:
                if l[i] <= l[j] and l[j] <= r[i]:
                    count += 1
                elif l[j] <= l[i] and l[i] <= r[j]:
                    count += 1
            elif t[i] == 2 and t[j] == 2:
                if l[i] <= l[j] and l[j] < r[i]:
                    count += 1
                elif l[j] < l[i] and l[i] <= r[j]:
                    count += 1
            elif t[i] == 2 and t[j] == 3:
                if l[i] < l[j] and l

=======
Suggestion 4

def main():
    N = int(input())
    intervals = []
    for i in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            intervals.append((l, r))
        elif t == 2:
            intervals.append((l, r - 1))
        elif t == 3:
            intervals.append((l + 1, r))
        else:
            intervals.append((l + 1, r - 1))
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if intervals[i][1] < intervals[j][0] or intervals[j][1] < intervals[i][0]:
                continue
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    intervals = []
    for i in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            intervals.append([l, r])
        elif t == 2:
            intervals.append([l, r - 1])
        elif t == 3:
            intervals.append([l + 1, r])
        else:
            intervals.append([l + 1, r - 1])

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if intervals[i][0] <= intervals[j][1] and intervals[i][1] >= intervals[j][0]:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    tlr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if tlr[i][0] == 1:
                if tlr[j][0] == 1:
                    if tlr[i][1] <= tlr[j][2] and tlr[j][1] <= tlr[i][2]:
                        cnt += 1
                elif tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][2] and tlr[j][1] < tlr[i][2]:
                        cnt += 1
                elif tlr[j][0] == 3:
                    if tlr[i][1] < tlr[j][2] and tlr[j][1] <= tlr[i][2]:
                        cnt += 1
                else:
                    if tlr[i][1] < tlr[j][2] and tlr[j][1] < tlr[i][2]:
                        cnt += 1
            elif tlr[i][0] == 2:
                if tlr[j][0] == 1:
                    if tlr[i][1] < tlr[j][2] and tlr[j][1] <= tlr[i][2]:
                        cnt += 1
                elif tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][2] and tlr[j][1] < tlr[i][2]:
                        cnt += 1
                elif tlr[j][0] == 3:
                    if tlr[i][1] < tlr[j][2] and tlr[j][1] < tlr[i][2]:
                        cnt += 1
                else:
                    if tlr[i][1] < tlr[j][2] and tlr[j][1] < tlr[i][2]:
                        cnt += 1
            elif tlr[i][0] == 3:
                if tlr[j][0] == 1:
                    if tlr[i][1] <= tlr[j][2] and tlr[j][1] < tlr[i][2]:
                        cnt += 1
                elif tlr[j][0]

=======
Suggestion 7

def main():
    n = int(input())
    tlr = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if tlr[i][0] == 1:
                if tlr[j][0] == 1:
                    if tlr[i][1] <= tlr[j][1] <= tlr[i][2]:
                        ans += 1
                    elif tlr[i][1] <= tlr[j][2] <= tlr[i][2]:
                        ans += 1
                elif tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] <= tlr[i][2]:
                        ans += 1
                    elif tlr[i][1] < tlr[j][2] <= tlr[i][2]:
                        ans += 1
                elif tlr[j][0] == 3:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2]:
                        ans += 1
                    elif tlr[i][1] < tlr[j][2] <= tlr[i][2]:
                        ans += 1
                elif tlr[j][0] == 4:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2]:
                        ans += 1
                    elif tlr[i][1] < tlr[j][2] < tlr[i][2]:
                        ans += 1
            elif tlr[i][0] == 2:
                if tlr[j][0] == 1:
                    if tlr[i][1] <= tlr[j][1] <= tlr[i][2]:
                        ans += 1
                    elif tlr[i][1] < tlr[j][2] <= tlr[i][2]:
                        ans += 1
                elif tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] < tlr[i][2]:
                        ans += 1
                    elif tlr[i][1] < tlr[j][2] < tlr[i][2]:
                        ans += 1
                elif tlr[j][0] == 3:
                    if tlr[i][1

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    for i in range(N):
        t,l,r = map(int,input().split())
        A.append([t,l,r])
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if A[i][0] == 1 and A[j][0] == 1:
                if A[i][1] <= A[j][1] <= A[i][2] or A[j][1] <= A[i][1] <= A[j][2]:
                    ans += 1
            elif A[i][0] == 2 and A[j][0] == 2:
                if A[i][1] < A[j][1] < A[i][2] or A[j][1] < A[i][1] < A[j][2]:
                    ans += 1
            elif A[i][0] == 3 and A[j][0] == 3:
                if A[i][1] < A[j][1] <= A[i][2] or A[j][1] < A[i][1] <= A[j][2]:
                    ans += 1
            elif A[i][0] == 4 and A[j][0] == 4:
                if A[i][1] < A[j][1] < A[i][2] or A[j][1] < A[i][1] < A[j][2]:
                    ans += 1
            elif A[i][0] == 1 and A[j][0] == 2:
                if A[i][1] <= A[j][1] < A[i][2]:
                    ans += 1
            elif A[i][0] == 2 and A[j][0] == 1:
                if A[j][1] <= A[i][1] < A[j][2]:
                    ans += 1
            elif A[i][0] == 1 and A[j][0] == 3:
                if A[i][1] <= A[j][1] <= A[i][2]:
                    ans += 1
            elif A[i][0] == 3 and A[j][0] == 1:
                if A[j][1] <= A[i][1] <= A[j][2]:
                    ans += 1
            elif A[i][0]

=======
Suggestion 9

def main():
    N=int(input())
    left=[0]*N
    right=[0]*N
    for i in range(N):
        t,l,r=map(int,input().split())
        if t==1:
            left[i]=l
            right[i]=r
        elif t==2:
            left[i]=l
            right[i]=r-1
        elif t==3:
            left[i]=l+1
            right[i]=r
        else:
            left[i]=l+1
            right[i]=r-1
    count=0
    for i in range(N-1):
        for j in range(i+1,N):
            if left[i]<=right[j] and left[j]<=right[i]:
                count+=1
    print(count)

=======
Suggestion 10

def main():
    N = int(input())
    #print(N)
    intervals = []
    for i in range(N):
        t, l, r = map(int, input().split())
        #print(t, l, r)
        intervals.append((t, l, r))
    #print(intervals)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            #print(i, j)
            ans += intersect(intervals[i], intervals[j])
    print(ans)
