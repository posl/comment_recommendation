Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    dis = []
    for i in range(m - 1):
        dis.append(x[i + 1] - x[i])
    dis.sort()
    print(sum(dis[:m - n]))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    d = [0] * (M-1)
    for i in range(M-1):
        d[i] = X[i+1] - X[i]
    d.sort()
    print(sum(d[:M-N]))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return

    dist = []
    for i in range(1, m):
        dist.append(x[i] - x[i-1])
    dist.sort()
    print(sum(dist[:m-n]))

=======
Suggestion 4

def main():
    n,m=map(int,input().split())
    x=list(map(int,input().split()))
    x.sort()
    if(n>=m):
        print(0)
        return
    l=[]
    for i in range(m-1):
        l.append(x[i+1]-x[i])
    l.sort()
    print(sum(l[:m-n]))

=======
Suggestion 5

def main():
    # 读取输入
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    # 排序
    x.sort()
    # 计算棋子间距
    distance = [0] * (m - 1)
    for i in range(m - 1):
        distance[i] = x[i + 1] - x[i]
    # 排序
    distance.sort()
    # 计算差值
    ans = 0
    for i in range(m - n):
        ans += distance[i]
    # 输出
    print(ans)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    # print(x)
    if n >= m:
        print(0)
        return
    if n == 1:
        print(x[m-1]-x[0])
        return
    # print(x)
    # print(x[n-1]-x[0])
    # print(x[m-1]-x[n])
    # print(min(x[m-1]-x[0],x[n-1]-x[0],x[m-1]-x[n]))
    print(min(x[m-1]-x[0],x[n-1]-x[0],x[m-1]-x[n]))

main()

=======
Suggestion 7

def solve(n,m,x):
    x.sort()
    if n == 1:
        return 0
    if n == 2:
        return x[1]-x[0]
    if n == 3:
        return x[2]-x[0]
    return x[n-1]-x[0]

=======
Suggestion 8

def main():
    # input
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    # solve
    x.sort()
    if n == 1:
        print(min(abs(x[0]-x[m-1]),abs(x[0]-x[1])))
    else:
        print(min(abs(x[0]-x[m-1]),abs(x[1]-x[m-1]),abs(x[0]-x[m-2]),abs(x[1]-x[m-2])))

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()

    if n >= m:
        print(0)
        return

    if n == 1:
        print(min(abs(x[i] - x[i + n - 1]) for i in range(m - n + 1)))
        return

    if n == 2:
        print(min(abs(x[i] - x[i + n - 1]) + abs(x[i + n - 1] - x[i + n]) for i in range(m - n + 2)))
        return

    print(min(abs(x[i] - x[i + n - 1]) + abs(x[i + n - 1] - x[i + n]) + abs(x[i + n] - x[i + n + 1]) for i in range(m - n + 3)))

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    distance = []
    for i in range(1, m):
        distance.append(x[i] - x[i - 1])
    distance.sort()
    print(sum(distance[:m - n]))
