Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve():
    pass

=======
Suggestion 3

def solve():
    N, D = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(N)]
    LRs.sort(key=lambda x: x[0])
    LRs = [[0, 0]] + LRs
    LRs.append([10 ** 9 + 1, 10 ** 9 + 1])
    ans = 0
    for i in range(1, N + 2):
        if LRs[i][0] - LRs[i - 1][1] >= D:
            ans += 1
        elif LRs[i][0] - LRs[i - 1][1] < D and LRs[i][0] - LRs[i - 1][1] > 0:
            ans += 2
        else:
            pass
    print(ans)

=======
Suggestion 4

def main():
    n,d = map(int,input().split())
    lst = []
    for i in range(n):
        l,r = map(int,input().split())
        lst.append([l,r])
    lst.sort()
    #print(lst)
    if n == 1:
        print(1)
        return
    ans = 1
    l = lst[0][0]
    r = lst[0][1]
    for i in range(1,n):
        if lst[i][0] > r:
            l = lst[i][0]
            r = lst[i][1]
            ans += 1
        else:
            l = max(l,lst[i][0])
            r = min(r,lst[i][1])
    print(ans)
    return

=======
Suggestion 5

def solve(n,d,wall):
    #wall = sorted(wall,key=lambda x:x[0])
    r = 0
    for i in range(n):
        if i == n-1:
            r += (wall[i][1] - wall[i][0] + d) // d
        else:
            r += (wall[i][1] - wall[i][0] + d) // d - 1
    return r

n,d = map(int,input().split())
wall = []
for i in range(n):
    l,r = map(int,input().split())
    wall.append([l,r])
print(solve(n,d,wall))

=======
Suggestion 6

def main():
    n,d=map(int,input().split())
    l=[]
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort(key=lambda x:x[0])
    count=1
    for i in range(n-1):
        if l[i][1]>l[i+1][0]:
            count+=1
    print(count)

=======
Suggestion 7

def solve(n, d, lr):
    lr.sort()
    ans = 0
    p = 0
    for i in range(n):
        l, r = lr[i]
        if p < l:
            p = l
        if r - p + 1 < d:
            continue
        ans += 1
        p += d
    return ans

n, d = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, d, lr))

=======
Suggestion 8

def solve():
    # 读入数据
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    # 求出所有墙的左右端点
    L_all = []
    R_all = []
    for i in range(N):
        L_all.append(L[i])
        R_all.append(R[i])
        L_all.append(L[i] - D)
        R_all.append(R[i] - D)
    L_all.sort()
    R_all.sort()

    # 从最左端开始，依次求出各个墙的所需打孔次数
    ans = 0
    l = 0
    r = 0
    for i in range(len(L_all)):
        while r < len(R_all) and R_all[r] <= L_all[i]:
            r += 1
        ans = max(ans, r - l)
        if L_all[i] == R_all[l]:
            l += 1
    print(ans)


solve()

=======
Suggestion 9

def f(n,d):
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort(key=lambda x:x[0])
    r = 0
    for i in range(n):
        if i == 0:
            r += (l[i][1] - l[i][0]) // d + 1
        else:
            if l[i][0] <= l[i - 1][1]:
                r += (l[i][1] - l[i - 1][1]) // d
                if (l[i][1] - l[i - 1][1]) % d == 0:
                    r -= 1
            else:
                r += (l[i][1] - l[i][0]) // d + 1
    print(r)

n,d = map(int,input().split())
f(n,d)
