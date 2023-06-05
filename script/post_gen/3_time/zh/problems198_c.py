Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def problems198_c():
    pass

=======
Suggestion 3

def main():
    R,X,Y = map(int,input().split())
    if X**2 + Y**2 < R**2:
        print(2)
    else:
        print(int((X**2+Y**2)**0.5/R)+1)

=======
Suggestion 4

def solution():
    R,X,Y = map(int,input().split())
    if X**2 + Y**2 < R**2:
        print(2)
    else:
        print(int((X**2 + Y**2)**0.5//R)+1)

=======
Suggestion 5

def solve():
    pass

=======
Suggestion 6

def main():
    r,x,y = map(int,input().split())
    if x**2 + y**2 < r**2:
        print(2)
    else:
        print(int((x**2 + y**2)**(1/2)//r) + 1)

=======
Suggestion 7

def get_min_step(r, x, y):
    #步数
    step = 0
    #当前位置
    cur_x, cur_y = 0, 0
    while True:
        #到达终点
        if cur_x == x and cur_y == y:
            break
        #到达终点
        if cur_x == x and cur_y == -y:
            break
        #到达终点
        if cur_x == -x and cur_y == y:
            break
        #到达终点
        if cur_x == -x and cur_y == -y:
            break
        #到达终点
        if cur_x == y and cur_y == x:
            break
        #到达终点
        if cur_x == y and cur_y == -x:
            break
        #到达终点
        if cur_x == -y and cur_y == x:
            break
        #到达终点
        if cur_x == -y and cur_y == -x:
            break
        #到达终点
        if cur_x == x and cur_y == 0:
            break
        #到达终点
        if cur_x == 0 and cur_y == y:
            break
        #到达终点
        if cur_x == -x and cur_y == 0:
            break
        #到达终点
        if cur_x == 0 and cur_y == -y:
            break
        #到达终点
        if cur_x == y and cur_y == 0:
            break
        #到达终点
        if cur_x == 0 and cur_y == -y:
            break
        #到达终点
        if cur_x == -y and cur_y == 0:
            break
        #到达终点
        if cur_x == 0 and cur_y == -y:
            break
        #到达终点
        if cur_x == y and cur_y == 0:
            break
        #到达终点
        if cur_x == 0 and cur_y == y:
            break
        #到达终点
        if cur_x == -x and cur_y == 0
