Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x,y,r = input().split(' ')
    x = float(x)
    y = float(y)
    r = float(r)
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    count = 0
    for i in range(x-r,x+r+1):
        for j in range(y-r,y+r+1):
            if (i-x)**2 + (j-y)**2 <= r**2:
                count += 1
    print(count)

=======
Suggestion 2

def problem191_d():
    x,y,r = map(float,input().split())
    x,y,r = int(x*10000),int(y*10000),int(r*10000)
    count = 0
    for i in range(x-r,x+r+1):
        for j in range(y-r,y+r+1):
            if (i-x)*(i-x)+(j-y)*(j-y) <= r*r:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    # 读入数据
    X, Y, R = map(float, input().split())
    # 计算圆内网格点的数量
    ans = 0
    for x in range(int(X - R), int(X + R) + 1):
        for y in range(int(Y - R), int(Y + R) + 1):
            if (X - x) ** 2 + (Y - y) ** 2 <= R ** 2:
                ans += 1
    # 输出答案
    print(ans)

=======
Suggestion 4

def solve():
    x, y, r = map(float, input().split())
    x, y, r = int(x*10000), int(y*10000), int(r*10000)
    ans = 0
    for i in range(y-r, y+r+1):
        for j in range(x-r, x+r+1):
            if (i-y)**2 + (j-x)**2 <= r**2:
                ans += 1
    print(ans)
solve()

=======
Suggestion 5

def main():
    x, y, r = map(float, input().split())
    ans = 0
    for i in range(int(x - r), int(x + r) + 1):
        for j in range(int(y - r), int(y + r) + 1):
            if (i - x) * (i - x) + (j - y) * (j - y) <= r * r:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    x,y,r = map(float,input().split())
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    x1 = x-r
    x2 = x+r
    y1 = y-r
    y2 = y+r
    count = 0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if (i-x)**2+(j-y)**2<=r**2:
                count += 1
    print(count)

=======
Suggestion 7

def main():
    X,Y,R = map(float,input().split())
    X = int(X*10000)
    Y = int(Y*10000)
    R = int(R*10000)
    ans = 0
    for i in range(int(X-R),int(X+R+1)):
        for j in range(int(Y-R),int(Y+R+1)):
            if (i-X)**2+(j-Y)**2 <= R**2:
                ans += 1
    print(ans)

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

=======
Suggestion 9

def count_point(x,y,r):
    count = 0
    for i in range(int(x-r),int(x+r)+1):
        for j in range(int(y-r),int(y+r)+1):
            if (i-x)**2+(j-y)**2 <= r**2:
                count += 1
    return count

x,y,r = map(float,input().split())
print(count_point(x,y,r))

=======
Suggestion 10

def main():
    x,y,r = map(float,input().split())
    x = int(x*10000)
    y = int(y*10000)
    r = int(r*10000)
    r2 = r*r
    ans = 0
    for i in range(x-r,x+r+1):
        for j in range(y-r,y+r+1):
            if (i-x)*(i-x)+(j-y)*(j-y)<=r2:
                ans += 1
    print(ans)
