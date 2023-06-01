Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print(type(N), type(M))
    #print((N, M))
    #print(type((N, M)))
    #print((N, M)[0])
    #print((N, M)[1])
    #print(type((N, M)[0]), type((N, M)[1]))
    #print((N, M)[0], (N, M)[1])
    #print((N, M)[0] * (N, M)[1])
    #print(type((N, M)[0] * (N, M)[1]))
    #print((N, M)[0] * (N, M)[1] * (N, M)[1])
    #print(type((N, M)[0] * (N, M)[1] * (N, M)[1]))
    #print((N, M)[0] * (N, M)[1] * (N, M)[1] * (N, M)[1])
    #print(type((N, M)[0] * (N, M)[1] * (N, M)[1] * (N, M)[1]))
    #print((N, M)[0] * (N, M)[1] * (N, M)[1] * (N, M)[1] * (N, M)[1])
    #print(type((N, M)[0]

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def dist(x,y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                print(0, end=' ')
            else:
                print(-1, end=' ')
        print()

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    if n == 1:
        print(0)
        return
    if n == 2:
        print(-1)
        return
    if n == 3:
        if m == 1:
            print("0 1 2")
            print("1 2 3")
            print("2 3 4")
            return
        if m == 2:
            print("0 1 2")
            print("1 2 1")
            print("2 1 2")
            return
        if m == 3:
            print("0 1 2")
            print("1 2 3")
            print("2 3 2")
            return
        if m == 4:
            print("0 1 2")
            print("1 2 3")
            print("2 3 4")
            return
        if m == 5:
            print("0 1 2")
            print("1 2 3")
            print("2 3 4")
            return
        if m == 6:
            print("0 1 2")
            print("1 2 3")
            print("2 3 4")
            return
        if m == 7:
            print("0 1 2")
            print("1 2 3")
            print("2 3 4")
            return
        if m == 8:
            print("0 1 2")
            print("1 2 3")
            print("2 3 4")
            return
        if m == 9:
            print("0 1 2")
            print("1 2 3")
            print("2 3 4")
            return
        if m == 10:
            print("0 1 2")
            print("1 2 3")
            print("2 3 4")
            return
    if n == 4:
        if m == 1:
            print("0 1 2 3")
            print("1 2 3 4")
            print("2 3 4 5")
            print("3 4 5 6")
            return
        if m == 2:
            print("0 1 2 3")
            print

=======
Suggestion 7

def main():
    # 读入数据
    n, m = map(int, input().split())
    # 计算距离
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = ((i + 1) - 1) ** 2 + ((j + 1) - 1) ** 2
    # 计算结果
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] <= m:
                ans[i][j] = 1
            else:
                ans[i][j] = -1
    # 打印结果
    for i in range(n):
        for j in range(n):
            print(ans[i][j], end=' ')
        print()

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    for i in range(N):
        for j in range(N):
            if i == j:
                print(0, end=' ')
            elif i < j:
                print(i + j, end=' ')
            else:
                print(j + i, end=' ')
        print()

=======
Suggestion 9

def main():
    print("Hello World!")
