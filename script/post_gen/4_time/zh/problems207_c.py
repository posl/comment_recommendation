Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    tlr = []
    for i in range(N):
        t, l, r = map(int, input().split())
        tlr.append([t, l, r])
    # print(tlr)
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if tlr[i][1] <= tlr[j][1] <= tlr[i][2] or tlr[j][1] <= tlr[i][1] <= tlr[j][2]:
                cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    n = int(input())
    tlr = []
    for i in range(n):
        tlr.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if (tlr[i][1] <= tlr[j][1] <= tlr[i][2]) or (tlr[i][1] <= tlr[j][2] <= tlr[i][2]) or (tlr[j][1] <= tlr[i][1] <= tlr[j][2]) or (tlr[j][1] <= tlr[i][2] <= tlr[j][2]):
                ans += 1
    print(ans)

main()

=======
Suggestion 3

def main():
    n = int(input())
    l = []
    for i in range(n):
        t, l1, l2 = map(int, input().split())
        if t == 1:
            l.append([l1, l2])
        elif t == 2:
            l.append([l1, l2-1])
        elif t == 3:
            l.append([l1+1, l2])
        elif t == 4:
            l.append([l1+1, l2-1])
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if l[i][0] <= l[j][1] and l[j][0] <= l[i][1]:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    tlr = []
    for i in range(N):
        tlr.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if tlr[i][0] == 1 or tlr[i][0] == 2:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] and tlr[i][2] >= tlr[j][1]:
                        count += 1
                else:
                    if tlr[i][1] <= tlr[j][1] and tlr[i][2] > tlr[j][1]:
                        count += 1
            else:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][1] and tlr[i][2] >= tlr[j][1]:
                        count += 1
                else:
                    if tlr[i][1] < tlr[j][1] and tlr[i][2] > tlr[j][1]:
                        count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    tlr_list = []
    for i in range(N):
        tlr_list.append(list(map(int, input().split())))

    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if tlr_list[i][2] >= tlr_list[j][1] and tlr_list[i][1] <= tlr_list[j][2]:
                count += 1
    print(count)

=======
Suggestion 6

def get_intersection(l1, r1, l2, r2):
    if r1 < l2 or r2 < l1:
        return 0
    else:
        return min(r1, r2) - max(l1, l2) + 1

n = int(input())
t = []
l = []
r = []
for i in range(n):
    t_i, l_i, r_i = map(int, input().split())
    t.append(t_i)
    l.append(l_i)
    r.append(r_i)

res = 0
for i in range(n):
    for j in range(i+1, n):
        if t[i] == 1 or t[i] == 3:
            if t[j] == 1 or t[j] == 2:
                res += get_intersection(l[i], r[i], l[j], r[j])
        elif t[i] == 2 or t[i] == 4:
            if t[j] == 3 or t[j] == 4:
                res += get_intersection(l[i], r[i], l[j], r[j])

print(res)

=======
Suggestion 7

def main():
    N = int(input())
    tlr = []
    for i in range(N):
        tlr.append(list(map(int,input().split())))
    cnt=0
    for i in range(N-1):
        for j in range(i+1,N):
            if tlr[i][2]>=tlr[j][1] and tlr[i][1]<=tlr[j][2]:
                cnt+=1
    print(cnt)

=======
Suggestion 8

def main():
    n = int(input())
    intervals = []
    for i in range(n):
        t, l, r = map(int, input().split())
        if t == 1:
            intervals.append([l, r])
        elif t == 2:
            intervals.append([l, r - 0.5])
        elif t == 3:
            intervals.append([l + 0.5, r])
        else:
            intervals.append([l + 0.5, r - 0.5])
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            if intervals[i][0] <= intervals[j][0] <= intervals[i][1] or intervals[j][0] <= intervals[i][0] <= intervals[j][1]:
                result += 1
    print(result)

=======
Suggestion 9

def main():
    N = int(input())
    tlr = [[int(x) for x in input().split()] for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (tlr[i][1] <= tlr[j][1] <= tlr[i][2]) or (tlr[i][1] <= tlr[j][2] <= tlr[i][2]) or (tlr[j][1] <= tlr[i][1] <= tlr[j][2]) or (tlr[j][1] <= tlr[i][2] <= tlr[j][2]):
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    tlr = [list(map(int,input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            t1,l1,r1 = tlr[i]
            t2,l2,r2 = tlr[j]
            if t1 in [1,2] and t2 in [1,2]:
                if l2 <= r1 and l1 <= r2:
                    ans += 1
            elif t1 in [1,2] and t2 in [3,4]:
                if l2 < r1 and l1 <= r2:
                    ans += 1
            elif t1 in [3,4] and t2 in [1,2]:
                if l2 <= r1 and l1 < r2:
                    ans += 1
            elif t1 in [3,4] and t2 in [3,4]:
                if l2 < r1 and l1 < r2:
                    ans += 1
    print(ans)
