Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    d_list = []
    for i in range(n):
        d_list.append(x_list[i+1] - x_list[i])
    import math
    ans = d_list[0]
    for i in range(1, n):
        ans = math.gcd(ans, d_list[i])
    print(ans)

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, x = map(int, input().split())
x_list = list(map(int, input().split()))
x_list.append(x)
x_list.sort()
diff_list = [x_list[i] - x_list[i-1] for i in range(1, n+1)]
diff_list.sort()
gcd_num = diff_list[0]
for i in range(1, n):
    gcd_num = gcd(gcd_num, diff_list[i])
print(gcd_num)

=======
Suggestion 3

def main():
    N,X = map(int,input().split())
    x = list(map(int,input().split()))
    x.append(X)
    x.sort()
    d = [x[i+1] - x[i] for i in range(N)]
    import math
    def gcd(a,b):
        while b:
            a,b = b,a%b
        return a
    def lcm(a,b):
        return a*b//gcd(a,b)
    ans = d[0]
    for i in range(1,N):
        ans = gcd(ans,d[i])
    print(ans)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    xlist = list(map(int, input().split()))
    xlist.append(x)
    xlist.sort()
    xlist = [xlist[i+1]-xlist[i] for i in range(n)]
    print(gcd_list(xlist))

=======
Suggestion 5

def main():
    #读取数据
    n,x = map(int,input().split())
    x_list = list(map(int,input().split()))
    x_list.append(x)
    x_list.sort()
    #计算两个相邻城市的距离
    dis = []
    for i in range(n):
        dis.append(x_list[i+1]-x_list[i])
    #求最大公约数
    def gcd(a,b):
        if a<b:
            a,b = b,a
        while b!=0:
            a,b = b,a%b
        return a
    #求最大公约数的函数
    def gcd_list(numbers):
        return reduce(gcd,numbers)
    #求最大公约数
    print(gcd_list(dis))

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 7

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

N, X = map(int, input().split())
x = list(map(int, input().split()))

x.append(X)
x.sort()

d = []
for i in range(N):
    d.append(x[i+1]-x[i])

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = []
    for i in range(N):
        d.append(x[i+1] - x[i])
    import math
    def gcd(a,b):
        if b == 0:
            return a
        else:
            return gcd(b, a%b)
    ans = d[0]
    for i in range(1, N):
        ans = gcd(ans, d[i])
    print(ans)

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    x_diff = [x_list[i+1] - x_list[i] for i in range(n)]
    x_diff.sort()
    if len(x_diff) == 1:
        print(x_diff[0])
    else:
        x_diff.remove(max(x_diff))
        print(max(x_diff))

=======
Suggestion 10

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

n,x=map(int,input().split())
a=list(map(int,input().split()))
a.append(x)
a.sort()
d=a[1]-a[0]
for i in range(2,n+1):
    d=gcd(d,a[i]-a[i-1])
print(d)
