Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    tlr = []
    for i in range(N):
        tlr.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if tlr[i][1] <= tlr[j][2] and tlr[j][1] <= tlr[i][2]:
                count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    tlr = []
    for i in range(n):
        tlr.append(list(map(int,input().split())))
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if tlr[i][1] <= tlr[j][2] and tlr[j][1] <= tlr[i][2]:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    tlr = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if tlr[i][1]<=tlr[j][1]<=tlr[i][2] or tlr[i][1]<=tlr[j][2]<=tlr[i][2] or tlr[j][1]<=tlr[i][1]<=tlr[j][2] or tlr[j][1]<=tlr[i][2]<=tlr[j][2]:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    # 读入数据
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    
    # 计算相交的区间
    count = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if (data[i][1] <= data[j][1] and data[j][1] <= data[i][2]) or \
                (data[j][1] <= data[i][1] and data[i][1] <= data[j][2]):
                count += 1
    
    # 输出结果
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    tlr = []
    for i in range(n):
        tlr.append(list(map(int,input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if (tlr[i][1] <= tlr[j][1] and tlr[j][1] <= tlr[i][2]) or (tlr[i][1] <= tlr[j][2] and tlr[j][2] <= tlr[i][2]) or (tlr[j][1] <= tlr[i][1] and tlr[i][1] <= tlr[j][2]) or (tlr[j][1] <= tlr[i][2] and tlr[i][2] <= tlr[j][2]):
                ans += 1
    print(ans)

=======
Suggestion 6

def func(l,r):
    if l[0]==1:
        if r[0]==1:
            return 1
        elif r[0]==2:
            return 1
        elif r[0]==3:
            return 0
        else:
            return 0
    elif l[0]==2:
        if r[0]==1:
            return 1
        elif r[0]==2:
            return 1
        elif r[0]==3:
            return 1
        else:
            return 0
    elif l[0]==3:
        if r[0]==1:
            return 0
        elif r[0]==2:
            return 1
        elif r[0]==3:
            return 1
        else:
            return 0
    else:
        if r[0]==1:
            return 0
        elif r[0]==2:
            return 0
        elif r[0]==3:
            return 0
        else:
            return 0

=======
Suggestion 7

def main():
    n = int(input())
    tlr = []
    for i in range(n):
        tlr.append(list(map(int,input().split())))
    cnt = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if tlr[i][2] < tlr[j][1]:
                continue
            if tlr[j][2] < tlr[i][1]:
                continue
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    #读取数据
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int,input().split())))
    #遍历所有的组合
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if data[i][1] <= data[j][2] and data[i][2] >= data[j][1]:#判断是否相交
                count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    T = []
    for i in range(N):
        T.append(list(map(int,input().split())))
    
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            if T[i][1] <= T[j][1] and T[j][1] <= T[i][2]:
                cnt += 1
            elif T[i][1] <= T[j][2] and T[j][2] <= T[i][2]:
                cnt += 1
            elif T[j][1] <= T[i][1] and T[i][1] <= T[j][2]:
                cnt += 1
            elif T[j][1] <= T[i][2] and T[i][2] <= T[j][2]:
                cnt += 1
    print(cnt)

=======
Suggestion 10

def get_input():
    n = int(input())
    intervals = []
    for i in range(n):
        t, l, r = map(int, input().split())
        intervals.append((t, l, r))
    return n, intervals
