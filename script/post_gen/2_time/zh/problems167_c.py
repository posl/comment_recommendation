Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m,x = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    res

=======
Suggestion 2

def main():
    n,m,x = map(int,input().split())
    #n,m,x = 3,3,10
    #n,m,x = 3,3,10
    #n,m,x = 8,5,22
    #c = [60,70,50]
    #a = [[2,2,4],[8,7,9],[2,3,9]]
    #c = [100,100,100]
    #a = [[3,1,4],[1,5,9],[2,6,5]]
    #c = [100,164,334,234,541,235,394,872]
    #a = [[3,7,5,3,1],[4,5,2,7,8],[7,2,7,2,9],[4,7,2,8,2],[5,4,3,3,6],[4,8,6,9,7],[3,6,1,6,2],[8,4,3,7,2]]
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int,input().split())))
        #c.append(list(map(int,input().split())))
        a.append(c[i][1:])
        c[i] = c[i][0]
    #print(c)
    #print(a)
    #print(n,m,x)
    #print(c)
    #print(a)
    #print(c)
    #print(a)
    #print(n,m,x)
    #print(c)

=======
Suggestion 3

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    total_cost = float('inf')
    for i in range(1 << N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if i >> j & 1:
                cost += C[j]
                for k in range(M):
                    understanding[k] += A[j][k]
        if all(x >= X for x in understanding):
            total_cost = min(total_cost, cost)
    if total_cost == float('inf'):
        print(-1)
    else:
        print(total_cost)

=======
Suggestion 4

def main():
    n,m,x=map(int,input().split())
    l=[]
    for i in range(n):
        l.append(list(map(int,input().split())))
    #print(l)
    #print(n,m,x)
    #print(l[0][0])
    #print(l[0][1])
    #print(l[0][2])
    #print(l[0][3])
    #print(l[0][4])
    #print(l[0][5])
    #print(l[1][0])
    #print(l[1][1])
    #print(l[1][2])
    #print(l[1][3])
    #print(l[1][4])
    #print(l[1][5])
    #print(l[2][0])
    #print(l[2][1])
    #print(l[2][2])
    #print(l[2][3])
    #print(l[2][4])
    #print(l[2][5])
    #print(l[3][0])
    #print(l[3][1])
    #print(l[3][2])
    #print(l[3][3])
    #print(l[3][4])
    #print(l[3][5])
    #print(l[4][0])
    #print(l[4][1])
    #print(l[4][2])
    #print(l[4][3])
    #print(l[4][4])
    #print(l[4][5])
    #print(l[5][0])
    #print(l[5][1])
    #print(l[5][2])
    #print(l[5][3])
    #print(l[5][4])
    #print(l[5][5])
    #print(l[6][0])
    #print(l[6][1])
    #print(l[6][2])
    #print(l[6][3])
    #print(l[6][4])
    #print(l[6][5])
    #print(l[7][0])
    #print(l[7][1])
    #print(l[7][2])
    #print(l[7][3])
    #print(l[7][4])
    #print(l[7][5])
    #print(l[8][0])
    #print(l[8][1])
    #print(l[

=======
Suggestion 5

def solve(n, m, x, c, a):
    ans = 10**9
    for i in range(2**n):
        sum = 0
        level = [0]*m
        for j in range(n):
            if (i >> j) & 1:
                sum += c[j]
                for k in range(m):
                    level[k] += a[j][k]
        if min(level) >= x:
            ans = min(ans, sum)
    if ans == 10**9:
        return -1
    else:
        return ans

n, m, x = map(int, input().split())
c = []
a = []
for i in range(n):
    s = list(map(int, input().split()))
    c.append(s[0])
    a.append(s[1:])
print(solve(n, m, x, c, a))

=======
Suggestion 6

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    ans = 10**9
    for i in range(2**N):
        cost = 0
        understand = [0]*M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if min(understand) >= X:
            ans = min(ans, cost)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

=======
Suggestion 7

def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c_i, a_i = map(int, input().split())
        c.append(c_i)
        a.append(a_i)
    print(c)
    print(a)

=======
Suggestion 8

def main():
    # 读取输入
    line1 = input().split()
    n = int(line1[0])
    m = int(line1[1])
    x = int(line1[2])
    # print(n, m, x)

    # 读取书的信息
    books = []
    for i in range(n):
        line = input().split()
        books.append([int(line[0]), list(map(int, line[1:]))])
    # print(books)

    # 用于记录最小的花费
    min_cost = -1

    # 遍历所有的书的组合
    for i in range(1, 2 ** n):
        # 用于记录当前组合的总花费
        cost = 0
        # 用于记录当前组合对每个算法的理解水平
        understand = [0] * m

        # 遍历每本书
        for j in range(n):
            # 如果当前书在当前组合中
            if i & (1 << j):
                cost += books[j][0]
                for k in range(m):
                    understand[k] += books[j][1][k]

        # 判断当前组合是否满足要求
        if min(understand) >= x:
            # 如果当前组合满足要求，更新最小花费
            if min_cost == -1:
                min_cost = cost
            else:
                min_cost = min(min_cost, cost)

    print(min_cost)

=======
Suggestion 9

def solve():
    #读取输入
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)

    #枚举所有购买方案
    ans = float('inf')
    for i in range(2**N):
        cost = 0
        understand = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if min(understand) >= X:
            ans = min(ans, cost)

    #输出
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

=======
Suggestion 10

def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int, input().split())))
    for i in range(n):
        a.append(c[i][1:])
    #print(a)
    #print(c)
    #print(n, m, x)
    #print(a[0][0])
    #print(a[0][1])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[2][0])
    #print(a[2][1])
    #print(c[0][0])
    #print(c[0][1])
    #print(c[1][0])
    #print(c[1][1])
    #print(c[2][0])
    #print(c[2][1])
    #print(a[0][0])
    #print(a[0][1])
    #print(a[0][2])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[1][2])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[2][2])
    #print(a[3][0])
    #print(a[3][1])
    #print(a[3][2])
    #print(a[4][0])
    #print(a[4][1])
    #print(a[4][2])
    #print(a[5][0])
    #print(a[5][1])
    #print(a[5][2])
    #print(a[6][0])
    #print(a[6][1])
    #print(a[6][2])
    #print(a[7][0])
    #print(a[7][1])
    #print(a[7][2])
    #print(a[0][0] + a[1][0] + a[2][0] + a[3][0] + a[4][0] + a[5][0] + a[6][0] + a[7][0])
    #print(a[0][1] + a[1][1] + a[2][1] + a[3][1] + a[4][1] + a[5][
