Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    tlr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if tlr[i][1] <= tlr[j][2] and tlr[j][1] <= tlr[i][2]:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    tlr = []
    for i in range(N):
        tlr.append(list(map(int, input().split())))
    # print(tlr)
    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if tlr[i][1] <= tlr[j][1] <= tlr[i][2] or tlr[i][1] <= tlr[j][2] <= tlr[i][2] or tlr[j][1] <= tlr[i][1] <= tlr[j][2] or tlr[j][1] <= tlr[i][2] <= tlr[j][2]:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    tlr = []
    for i in range(n):
        tlr.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if tlr[i][0] == 1 or tlr[i][0] == 2:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] <= tlr[i][2] or tlr[i][1] <= tlr[j][2] <= tlr[i][2]:
                        ans += 1
                else:
                    if tlr[i][1] <= tlr[j][1] < tlr[i][2] or tlr[i][1] < tlr[j][2] <= tlr[i][2]:
                        ans += 1
            else:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][1] <= tlr[i][2] or tlr[i][1] <= tlr[j][2] < tlr[i][2]:
                        ans += 1
                else:
                    if tlr[i][1] < tlr[j][1] < tlr[i][2] or tlr[i][1] < tlr[j][2] < tlr[i][2]:
                        ans += 1
    print(ans)

=======
Suggestion 4

def solve():
    n = int(input())
    tlr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if tlr[i][0] == 1:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] <= tlr[j][1] and tlr[j][1] <= tlr[i][2]:
                        ans += 1
                else:
                    if tlr[i][1] <= tlr[j][1] and tlr[j][1] < tlr[i][2]:
                        ans += 1
            elif tlr[i][0] == 2:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][1] and tlr[j][1] <= tlr[i][2]:
                        ans += 1
                else:
                    if tlr[i][1] < tlr[j][1] and tlr[j][1] < tlr[i][2]:
                        ans += 1
            elif tlr[i][0] == 3:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][1] and tlr[j][1] <= tlr[i][2]:
                        ans += 1
                else:
                    if tlr[i][1] < tlr[j][1] and tlr[j][1] < tlr[i][2]:
                        ans += 1
            else:
                if tlr[j][0] == 1 or tlr[j][0] == 2:
                    if tlr[i][1] < tlr[j][1] and tlr[j][1] <= tlr[i][2]:
                        ans += 1
                else:
                    if tlr[i][1] < tlr[j][1] and tlr[j][1] < tlr[i][2]:
                        ans += 1
    print(ans)

=======
Suggestion 5

def get_input():
    N = int(input())
    tlr = []
    for i in range(N):
        tlr.append(list(map(int,input().split())))
    return N,tlr

=======
Suggestion 6

def get_input():
    n = int(input())
    input_list = []
    for i in range(n):
        t, l, r = map(int, input().split())
        input_list.append((t, l, r))
    return input_list

=======
Suggestion 7

def main():
    #读取输入
    N = int(input())
    #print(N)
    #初始化数组
    t = [0]*N
    l = [0]*N
    r = [0]*N
    #print(t,l,r)
    #循环读取
    for i in range(N):
        t[i],l[i],r[i] = map(int,input().split())
    #print(t,l,r)
    #计算
    count = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if (l[i]<=l[j] and l[j]<=r[i]) or (l[i]<=r[j] and r[j]<=r[i]) or (l[j]<=l[i] and l[i]<=r[j]) or (l[j]<=r[i] and r[i]<=r[j]):
                count += 1
    #输出
    print(count)

=======
Suggestion 8

def get_input():
    n = int(input())
    tlr = []
    for _ in range(n):
        tlr.append(list(map(int,input().split())))
    return n,tlr

=======
Suggestion 9

def main():
    N = int(input())
    tlr = []
    for i in range(N):
        tlr.append(list(map(int, input().split())))
    #print(tlr)
    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if tlr[i][0] == 1 and tlr[j][0] == 1:
                if tlr[i][1] <= tlr[j][1] and tlr[j][1] <= tlr[i][2]:
                    count += 1
                elif tlr[i][1] <= tlr[j][2] and tlr[j][2] <= tlr[i][2]:
                    count += 1
                elif tlr[j][1] <= tlr[i][1] and tlr[i][2] <= tlr[j][2]:
                    count += 1
            elif tlr[i][0] == 1 and tlr[j][0] == 2:
                if tlr[i][1] <= tlr[j][1] and tlr[j][1] < tlr[i][2]:
                    count += 1
                elif tlr[j][1] <= tlr[i][1] and tlr[i][2] < tlr[j][2]:
                    count += 1
            elif tlr[i][0] == 1 and tlr[j][0] == 3:
                if tlr[i][1] <= tlr[j][1] and tlr[j][1] <= tlr[i][2]:
                    count += 1
            elif tlr[i][0] == 1 and tlr[j][0] == 4:
                if tlr[i][1] <= tlr[j][1] and tlr[j][1] < tlr[i][2]:
                    count += 1
            elif tlr[i][0] == 2 and tlr[j][0] == 1:
                if tlr[i][1] <= tlr[j][1] and tlr[j][1] < tlr[i][2]:
                    count += 1
                elif tlr[j][1] <= tlr[i][1] and tlr[i][2] < tlr[j][2]:
                    count += 1
            elif tlr[i][0] == 2

=======
Suggestion 10

def main():
    n = int(input())
    tlr = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if tlr[i][1] <= tlr[j][2] and tlr[j][1] <= tlr[i][2]:
                ans += 1
    print(ans)
