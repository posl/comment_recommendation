Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    r,x,y = map(int, input().split())
    if (x**2 + y**2) < r**2:
        print(2)
    else:
        print(-(-((x**2 + y**2)**(1/2))//r))

=======
Suggestion 2

def main():
    r,x,y = map(int,input().split())
    dis = (x**2 + y**2)**(1/2)
    if dis % r == 0:
        print(int(dis/r))
    elif dis < r:
        print(2)
    else:
        print(int(dis//r)+1)

=======
Suggestion 3

def cal(x,y):
    return (x**2+y**2)**0.5

r,x,y = map(int,input().split())
distance = cal(x,y)

=======
Suggestion 4

def main():
    r,x,y = map(int,input().split())
    if 0 == x and 0 == y:
        print(0)
    elif 0 == x or 0 == y:
        print(1)
    else:
        if r*r > x*x + y*y:
            print(2)
        else:
            print(int((x*x+y*y)**0.5/r) + 1)

=======
Suggestion 5

def main():
    r,x,y = map(int,input().split())
    if (x**2 + y**2) % (r**2) == 0:
        print((x**2 + y**2) // (r**2))
    else:
        print((x**2 + y**2) // (r**2) + 1)

=======
Suggestion 6

def min_step(r,x,y):
    if x**2 + y**2 < r**2:
        return 2
    else:
        return int((x**2 + y**2)**0.5/r) + 1

r,x,y = map(int,input().split())
print(min_step(r,x,y))

=======
Suggestion 7

def problem198_c():
    r,x,y = map(int, input().split())
    if r*r == (x*x + y*y):
        print(1)
    elif r*r > (x*x + y*y):
        print(2)
    else:
        print(int(((x*x + y*y)**(1/2) + r -1)/r))
    return

=======
Suggestion 8

def main():
    r, x, y = map(int, input().split())
    if (x * x + y * y) % (r * r) == 0:
        print((x * x + y * y) // (r * r))
    else:
        print((x * x + y * y) // (r * r) + 1)

=======
Suggestion 9

def main():
    # 读入数据
    R, X, Y = input().split()
    R = int(R)
    X = int(X)
    Y = int(Y)
    # 计算结果
    ans = 0
    # 1.求出从原点到目标点的距离
    dist = (X ** 2 + Y ** 2) ** 0.5
    # 2.用距离除以R，得到步数
    ans = dist // R
    # 3.判断是否有余数
    if dist % R != 0:
        ans += 1
    # 4.如果步数为1，且余数不为0，则步数加1
    if ans == 1 and dist % R != 0:
        ans += 1
    # 5.输出结果
    print(int(ans))

=======
Suggestion 10

def main():
    import math
    R, X, Y = map(int, input().split())
    d = math.sqrt(X**2 + Y**2)
    if d == R:
        print(1)
    elif d <= 2*R:
        print(2)
    else:
        print(math.ceil(d/R))
