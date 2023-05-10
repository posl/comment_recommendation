Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    tlr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if tlr[i][0] == 1:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] <= tlr[i][2]:
                        ans += 1
                else:
                    if tlr[i][1] <= tlr[j][1] < tlr[i][2]:
                        ans += 1
            elif tlr[i][0] == 2:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] < tlr[i][2]:
                        ans += 1
                else:
                    if tlr[i][1] <= tlr[j][1] < tlr[i][2]:
                        ans += 1
            elif tlr[i][0] == 3:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2]:
                        ans += 1
                else:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2]:
                        ans += 1
            else:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2]:
                        ans += 1
                else:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2]:
                        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    tlr = []
    for _ in range(n):
        tlr.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            t1, l1, r1 = tlr[i]
            t2, l2, r2 = tlr[j]
            if t1 == 1:
                if t2 == 1:
                    if l1 <= l2 <= r1:
                        ans += 1
                    elif l1 <= r2 <= r1:
                        ans += 1
                    elif l2 <= l1 <= r2:
                        ans += 1
                    elif l2 <= r1 <= r2:
                        ans += 1
                elif t2 == 2:
                    if l1 <= l2 < r1:
                        ans += 1
                    elif l1 <= r2 < r1:
                        ans += 1
                    elif l2 < l1 <= r2:
                        ans += 1
                    elif l2 < r1 <= r2:
                        ans += 1
                elif t2 == 3:
                    if l1 < l2 <= r1:
                        ans += 1
                    elif l1 < r2 <= r1:
                        ans += 1
                    elif l2 <= l1 < r2:
                        ans += 1
                    elif l2 <= r1 < r2:
                        ans += 1
                elif t2 == 4:
                    if l1 < l2 < r1:
                        ans += 1
                    elif l1 < r2 < r1:
                        ans += 1
                    elif l2 < l1 < r2:
                        ans += 1
                    elif l2 < r1 < r2:
                        ans += 1
            elif t1 == 2:
                if t2 == 1:
                    if l1 < l2 <= r1:
                        ans += 1
                    elif l1 < r2 <= r1:
                        ans += 1
                    elif l2 <= l1 < r2:
                        ans += 1
                    elif l2 <= r1 < r2:
                        ans += 1
                elif t2 == 2:
                    if l1 < l2 < r1:

=======
Suggestion 3

def main():
    N = int(input())
    TLR = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if TLR[i][1] > TLR[j][1]:
                TLR[i], TLR[j] = TLR[j], TLR[i]
            if TLR[i][2] >= TLR[j][1]:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    tlr = [list(map(int, input().split())) for _ in range(N)]
    #print(tlr)

    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            #print(tlr[i], tlr[j])
            if tlr[i][1] <= tlr[j][2] and tlr[j][1] <= tlr[i][2]:
                cnt += 1

    print(cnt)

=======
Suggestion 5

def main():
    N = int(input())
    #print(N)
    #N = 3
    #t = [1,2,3]
    #l = [1,2,2]
    #r = [2,3,4]
    t = []
    l = []
    r = []
    for i in range(N):
        tmp = input().split()
        t.append(int(tmp[0]))
        l.append(int(tmp[1]))
        r.append(int(tmp[2]))
    #print(t)
    #print(l)
    #print(r)
    #print(len(t))
    #print(len(l))
    #print(len(r))
    #print(t[0])
    #print(l[0])
    #print(r[0])
    #print(t[1])
    #print(l[1])
    #print(r[1])
    #print(t[2])
    #print(l[2])
    #print(r[2])
    #print(t[0] == 1)
    #print(t[0] == 2)
    #print(t[0] == 3)
    #print(t[0] == 4)
    #print(l[0] <= l[1])
    #print(l[0] <= r[1])
    #print(r[0] >= l[1])
    #print(r[0] >= r[1])
    #print(l[0] <= l[2])
    #print(l[0] <= r[2])
    #print(r[0] >= l[2])
    #print(r[0] >= r[2])
    #print(l[1] <= l[2])
    #print(l[1] <= r[2])
    #print(r[1] >= l[2])
    #print(r[1] >= r[2])
    #print(t[0])
    #print(t[1])
    #print(t[2])
    #print(l[0])
    #print(l[1])
    #print(l[2])
    #print(r[0])
    #print(r[1])
    #print(r[2])
    #print(t[0] == 1)
    #print(t[1] == 1)
    #print(t[2] == 1)
    #print(t[0] == 2)
    #print(t[1

=======
Suggestion 6

def main():
    n = int(input())
    tlr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if tlr[i][0] == 1 and tlr[j][0] == 1:
                if tlr[i][1] <= tlr[j][2] and tlr[j][1] <= tlr[i][2]:
                    ans += 1
            elif tlr[i][0] == 1 and tlr[j][0] == 2:
                if tlr[i][1] <= tlr[j][2] and tlr[j][1] < tlr[i][2]:
                    ans += 1
            elif tlr[i][0] == 1 and tlr[j][0] == 3:
                if tlr[i][1] <= tlr[j][2] and tlr[j][1] <= tlr[i][2]:
                    ans += 1
            elif tlr[i][0] == 1 and tlr[j][0] == 4:
                if tlr[i][1] <= tlr[j][2] and tlr[j][1] < tlr[i][2]:
                    ans += 1
            elif tlr[i][0] == 2 and tlr[j][0] == 1:
                if tlr[i][1] < tlr[j][2] and tlr[j][1] <= tlr[i][2]:
                    ans += 1
            elif tlr[i][0] == 2 and tlr[j][0] == 2:
                if tlr[i][1] < tlr[j][2] and tlr[j][1] < tlr[i][2]:
                    ans += 1
            elif tlr[i][0] == 2 and tlr[j][0] == 3:
                if tlr[i][1] < tlr[j][2] and tlr[j][1] <= tlr[i][2]:
                    ans += 1
            elif tlr[i][0] == 2 and tlr[j][0] == 4:
                if tlr[i][1] < tlr[j][2] and tlr[j][1] < tlr[i][2

=======
Suggestion 7

def main():
    N = int(input())
    tlr = [list(map(int,input().split())) for i in range(N)]
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if tlr[i][1] <= tlr[j][2] and tlr[j][1] <= tlr[i][2]:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    tlr = []
    for i in range(n):
        tlr.append(list(map(int, input().split())))

    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if tlr[i][0] == 1:
                if tlr[j][0] == 1:
                    if tlr[i][1] <= tlr[j][1] <= tlr[i][2]:
                        ans += 1
                    elif tlr[i][1] <= tlr[j][2] <= tlr[i][2]:
                        ans += 1
                    elif tlr[j][1] <= tlr[i][1] <= tlr[j][2]:
                        ans += 1
                    elif tlr[j][1] <= tlr[i][2] <= tlr[j][2]:
                        ans += 1
                elif tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] < tlr[i][2]:
                        ans += 1
                    elif tlr[i][1] <= tlr[j][2] <= tlr[i][2]:
                        ans += 1
                    elif tlr[j][1] <= tlr[i][1] < tlr[j][2]:
                        ans += 1
                    elif tlr[j][1] <= tlr[i][2] <= tlr[j][2]:
                        ans += 1
                elif tlr[j][0] == 3:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2]:
                        ans += 1
                    elif tlr[i][1] <= tlr[j][2] <= tlr[i][2]:
                        ans += 1
                    elif tlr[j][1] < tlr[i][1] <= tlr[j][2]:
                        ans += 1
                    elif tlr[j][1] <= tlr[i][2] <= tlr[j][2]:
                        ans += 1
                elif tlr[j][0] == 4:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2]:
                        ans += 1
                    elif tlr[i][1] < tlr[j][2] < t

=======
Suggestion 9

def main():
    N = int(input())
    data = []
    for i in range(N):
        t, l, r = map(int, input().split())
        data.append((t, l, r))
    #print(data)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if data[i][1] <= data[j][1] and data[j][1] <= data[i][2]:
                count += 1
            elif data[i][1] <= data[j][2] and data[j][2] <= data[i][2]:
                count += 1
            elif data[j][1] <= data[i][1] and data[i][1] <= data[j][2]:
                count += 1
            elif data[j][1] <= data[i][2] and data[i][2] <= data[j][2]:
                count += 1
    print(count)

=======
Suggestion 10

def main():
    N = int(input())
    tlr = []
    for _ in range(N):
        tlr.append(list(map(int, input().split())))

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if tlr[i][0] == 1:
                if tlr[j][0] == 1:
                    if tlr[i][1] <= tlr[j][1] <= tlr[i][2]:
                        ans += 1
                    elif tlr[i][1] <= tlr[j][2] <= tlr[i][2]:
                        ans += 1
                    elif tlr[j][1] <= tlr[i][1] <= tlr[j][2]:
                        ans += 1
                    elif tlr[j][1] <= tlr[i][2] <= tlr[j][2]:
                        ans += 1
                elif tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] < tlr[i][2]:
                        ans += 1
                    elif tlr[j][1] <= tlr[i][1] < tlr[j][2]:
                        ans += 1
                elif tlr[j][0] == 3:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2]:
                        ans += 1
                    elif tlr[j][1] < tlr[i][1] <= tlr[j][2]:
                        ans += 1
                elif tlr[j][0] == 4:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2]:
                        ans += 1
                    elif tlr[j][1] < tlr[i][1] < tlr[j][2]:
                        ans += 1
            elif tlr[i][0] == 2:
                if tlr[j][0] == 1:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2]:
                        ans += 1
                    elif tlr[j][1] < tlr[i][1] <= tlr[j][2]:
                        ans += 1
                elif tlr[j][0] == 2:
                    if tlr[i][1] <= tlr
