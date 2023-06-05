Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y, a, b = map(int, input().split())
    exp = 0
    while x * a < x + b and x * a < y:
        x *= a
        exp += 1
    exp += (y - 1 - x) // b
    print(exp)

=======
Suggestion 2

def solve():
    x, y, a, b = map(int, input().split())
    exp = 0
    while x < y:
        if x * a < x + b:
            x *= a
            exp += 1
        else:
            exp += (y - x - 1) // b
            break
    print(exp)

solve()

=======
Suggestion 3

def cal_max_exp(x, y, a, b):
    exp = 0
    while True:
        if (x * a) > (x + b):
            x *= a
            exp += 1
            if x >= y:
                break
        else:
            x += b
            exp += 1
            if x >= y:
                break
    return exp

=======
Suggestion 4

def problems180_d():
    x, y, a, b = map(int, input().split())
    cnt = 0
    while x*a < x+b and x*a < y:
        x *= a
        cnt += 1
    print(cnt + (y-1-x)//b)

=======
Suggestion 5

def main():
    x, y, a, b = map(int, input().split())
    exp = 0
    while True:
        if x * a < x + b and x * a < y:
            x *= a
            exp += 1
        else:
            exp += (y - x - 1) // b
            break
    print(exp)

=======
Suggestion 6

def problems180_d():
    pass

=======
Suggestion 7

def main():
    #读取数据
    x,y,a,b = map(int,input().split())
    #逻辑处理
    exp = 0
    while x*a <= x+b and x*a < y:
        exp += 1
        x *= a
    exp += (y-x-1)//b
    #输出结果
    print(exp)
    return 0

=======
Suggestion 8

def main():
    x, y, a, b = map(int, input().split())
    exp = 0
    while x*a < x+b and x*a < y:
        x *= a
        exp += 1
    exp += (y - x - 1) // b
    print(exp)

=======
Suggestion 9

def solve(x, y, a, b):
    exp = 0
    while x < y:
        if x * a < x + b:
            x *= a
        else:
            x += b
        exp += 1
    return exp
