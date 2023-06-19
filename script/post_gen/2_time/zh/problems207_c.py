Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    tlr = []
    for _ in range(n):
        tlr.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if tlr[i][1] <= tlr[j][1] and tlr[i][2] >= tlr[j][1]:
                ans += 1
            elif tlr[i][1] >= tlr[j][1] and tlr[i][1] <= tlr[j][2]:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if A[i][1] <= A[j][2] and A[j][1] <= A[i][2]:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    # n = int(input())
    # tlr = []
    # for i in range(n):
    #     tlr.append(list(map(int, input().split())))
    n = 19
    tlr = [[4, 210068409, 221208102],
           [4, 16698200, 910945203],
           [4, 76268400, 259148323],
           [4, 370943597, 566244098],
           [1, 428897569, 509621647],
           [4, 250946752, 823720939],
           [1, 642505376, 868415584],
           [2, 619091266, 868230936],
           [2, 306543999, 654038915],
           [4, 486033777, 715789416],
           [1, 527225177, 583184546],
           [2, 885292456, 900938599],
           [3, 264004185, 486613484],
           [2, 345310564, 818091848],
           [1, 152544274, 521564293],
           [4, 13819154, 555218434],
           [3, 507364086, 545932412],
           [4, 797872271, 935850549],
           [2, 415488246, 685203817]]
    # 1 2 3 4
    # 1 3 2 4
    # 1 4 2 3
    # 2 1 3 4
    # 2 3 1 4
    # 2 4 1 3
    # 3 1 2 4
    # 3 2 1 4
    # 3 4 1 2
    # 4 1 2 3
    # 4 2 1 3
    # 4 3 1 2
    # 1 2 3 4
    # 1 2 4 3
    # 1 3 4 2
    # 2 1 3 4
    # 2 1 4 3

=======
Suggestion 4

def main():
    N = int(input())
    tlr = []
    for i in range(N):
        tlr.append(list(map(int, input().split())))
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if (tlr[i][1] <= tlr[j][1] and tlr[j][1] <= tlr[i][2]) or (tlr[i][1] <= tlr[j][2] and tlr[j][2] <= tlr[i][2]) or (tlr[j][1] <= tlr[i][1] and tlr[i][1] <= tlr[j][2]) or (tlr[j][1] <= tlr[i][2] and tlr[i][2] <= tlr[j][2]):
                ans += 1
    print(ans)

=======
Suggestion 5

def count_intersection(n, intervals):
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if intervals[i][0] < intervals[j][0] < intervals[i][1] < intervals[j][1]:
                cnt += 1
            elif intervals[j][0] < intervals[i][0] < intervals[j][1] < intervals[i][1]:
                cnt += 1
    return cnt

=======
Suggestion 6

def get_list():
    N = int(input())
    list = []
    for i in range(N):
        t,l,r = map(int,input().split())
        list.append([t,l,r])
    return list

=======
Suggestion 7

def main():
    N = int(input())
    tlr = []
    for i in range(N):
        tlr.append(list(map(int,input().split())))
    count = 0
    for i in range(0,N):
        for j in range(i+1,N):
            if tlr[i][1] <= tlr[j][1] and tlr[j][1] <= tlr[i][2]:
                count += 1
            elif tlr[i][1] <= tlr[j][2] and tlr[j][2] <= tlr[i][2]:
                count += 1
            elif tlr[j][1] <= tlr[i][1] and tlr[i][1] <= tlr[j][2]:
                count += 1
            elif tlr[j][1] <= tlr[i][2] and tlr[i][2] <= tlr[j][2]:
                count += 1
    print(count)

=======
Suggestion 8

def get_input():
    N = int(input())
    tlr = []
    for i in range(N):
        tlr.append(list(map(int, input().split())))
    return N, tlr

=======
Suggestion 9

def main():
    N = int(input())
    tlr = [list(map(int, input().split())) for _ in range(N)]
    #print(tlr)
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if tlr[i][1] <= tlr[j][1] <= tlr[i][2] or tlr[i][1] <= tlr[j][2] <= tlr[i][2] or tlr[j][1] <= tlr[i][1] <= tlr[j][2] or tlr[j][1] <= tlr[i][2] <= tlr[j][2]:
                cnt += 1
    print(cnt)

=======
Suggestion 10

def get_area(t,l,r):
    if t == 1:
        return [l,r]
    elif t == 2:
        return [l,r-1]
    elif t == 3:
        return [l+1,r]
    else:
        return [l+1,r-1]
