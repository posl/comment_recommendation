Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    ans = 0
    for i in range(0, 10):
        if x + i * 10 >= y:
            ans = i
            break
    print(ans)

=======
Suggestion 2

def main():
    x,y = map(int,raw_input().split())
    if x >= y:
        print 0
    else:
        print (y-x)/10

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    print((y - x) // 10)

=======
Suggestion 4

def main():
    x,y = map(int,input().split())
    if x >= y:
        print(0)
        return
    else:
        print((y-x)//10)

=======
Suggestion 5

def get_input():
    x, y = map(int, input().split())
    return x, y

=======
Suggestion 6

def main():
    x,y=map(int,input().split())
    c=0
    while x<y:
        x+=10
        c+=1
    print(c)

=======
Suggestion 7

def main():
    # 读取输入
    x, y = map(int, input().split())
    # 计算差额
    diff = y - x
    # 计算最少需要贴多少张10元的邮票
    print(diff // 10)

=======
Suggestion 8

def solve():
    X, Y = map(int, input().split())
    print((Y - X) // 10)

=======
Suggestion 9

def main():
    x,y = map(int, input().split())
    print(0 if x >= y else (y - x) // 10)
