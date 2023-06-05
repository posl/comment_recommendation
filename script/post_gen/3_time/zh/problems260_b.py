Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([a[i]+b[i],a[i],i+1])
    c.sort(reverse=True)
    d = []
    for i in range(x):
        d.append(c[i])
    d.sort(key=lambda x:x[2])
    for i in range(y):
        d.append(c[x+i])
    d.sort(key=lambda x:x[2])
    for i in range(z):
        d.append(c[x+y+i])
    d.sort(key=lambda x:x[2])
    for i in range(len(d)):
        print(d[i][2])

=======
Suggestion 2

def main():
    # 输入
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    # 用于存储考生的总分和考生的编号
    c = []
    # 用于存储考生的编号
    d = []
    # 用于存储考生的总分
    e = []
    # 用于存储考生的总分和考生的编号
    f = []
    # 用于存储考生的编号
    g = []
    # 用于存储考生的总分
    h = []
    # 用于存储考生的总分和考生的编号
    i = []
    # 用于存储考生的编号
    j = []
    # 用于存储考生的总分
    k = []
    # 用于存储考生的总分和考生的编号
    l = []
    # 用于存储考生的编号
    m = []
    # 用于存储考生的总分
    n = []
    # 用于存储考生的总分和考生的编号
    o = []
    # 用于存储考生的编号
    p = []
    # 用于存储考生的总分
    q = []
    # 用于存储考生的总分和考生的编号
    r = []
    # 用于存储考生的编号
    s = []
    # 用于存储考生的总分
    t = []
    # 用于存储考生的总分和考生的编号
    u = []
    # 用于存储考生的编号
    v = []
    # 用于存储考生的总分
    w = []
    # 用于存储考生的总分和考生的编号
    x1 = []
    # 用于存储考生的编号
    y1 = []
    # 用于存储考生的总分

=======
Suggestion 3

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(zip(a,b))
    c.sort(key=lambda x: x[0],reverse=True)
    c = c[:x]
    c.sort(key=lambda x: x[1],reverse=True)
    c = c[:x+y]
    c.sort(key=lambda x: x[0]+x[1],reverse=True)
    c = c[:x+y+z]
    c.sort(key=lambda x: x[0])
    for i in range(len(c)):
        print(c[i][0]+1)

=======
Suggestion 4

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([a[i]+b[i],i+1])
    c.sort()
    c.reverse()
    for i in range(x):
        print(c[i][1])
    if y == 0:
        for i in range(x,x+z):
            print(c[i][1])
    else:
        for i in range(x,x+y):
            print(c[i][1])
        for i in range(x+y,x+y+z):
            print(c[i][1])

=======
Suggestion 5

def main():
    N, X, Y, Z = input().split()
    N = int(N)
    X = int(X)
    Y = int(Y)
    Z = int(Z)

    A = input().split()
    B = input().split()

    A = [int(A[i]) for i in range(N)]
    B = [int(B[i]) for i in range(N)]

    C = [i for i in range(N)]
    C.sort(key=lambda i: -A[i])
    C = C[:X]

    D = [i for i in range(N) if i not in C]
    D.sort(key=lambda i: -B[i])
    D = D[:Y]

    E = [i for i in range(N) if i not in C and i not in D]
    E.sort(key=lambda i: -(A[i] + B[i]))
    E = E[:Z]

    F = C + D + E
    F.sort()

    for i in F:
        print(i + 1)

=======
Suggestion 6

def main():
    # 读入数据
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 构造一个元组列表
    # 该元组列表的元素是 (总分, 数学分数, 英语分数, 序号)
    # 序号是为了在总分、数学分数和英语分数都相同时，按照序号的升序排列
    c = [(a[i] + b[i], a[i], b[i], i + 1) for i in range(n)]

    # 按照总分、数学分数和英语分数的顺序进行排序
    c.sort(reverse=True)

    # 按照题目要求，输出结果
    for i in range(x + y + z):
        print(c[i][3])

=======
Suggestion 7

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([a[i]+b[i],i+1])
    c = sorted(c,reverse=True)
    d = []
    for i in range(x):
        d.append(c[i][1])
    d = sorted(d)
    print(*d,sep="\n")
    c = c[x:]
    e = []
    for i in range(y):
        e.append(c[i][1])
    e = sorted(e)
    print(*e,sep="\n")
    c = c[y:]
    f = []
    for i in range(z):
        f.append(c[i][1])
    f = sorted(f)
    print(*f,sep="\n")
    c = c[z:]
    g = []
    for i in range(len(c)):
        g.append(c[i][1])
    g = sorted(g)
    print(*g,sep="\n")

=======
Suggestion 8

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    c = []
    for i in range(n):
        c.append([i+1,a[i],b[i],a[i]+b[i]])
    c.sort(key=lambda x:(-x[1],-x[2],-x[3],x[0]))
    for i in range(x):
        print(c[i][0])
    for i in range(y):
        print(c[x+i][0])
    for i in range(z):
        print(c[x+y+i][0])

=======
Suggestion 9

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = [(a[i],b[i],i+1) for i in range(n)]
    c.sort(key=lambda x:(x[0],x[2]),reverse=True)
    c = c[:x]
    c.sort(key=lambda x:(x[1],x[2]),reverse=True)
    c = c[:x+y]
    c.sort(key=lambda x:(x[0]+x[1],x[2]),reverse=True)
    c = c[:x+y+z]
    c.sort(key=lambda x:x[2])
    for i in c:
        print(i[2])

=======
Suggestion 10

def get_input():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    return N, X, Y, Z, A, B
