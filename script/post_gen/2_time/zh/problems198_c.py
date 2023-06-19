Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    R, X, Y = map(int, input().split())
    if (X**2 + Y**2) % (R**2) == 0:
        print((X**2 + Y**2) // (R**2))
    else:
        print((X**2 + Y**2) // (R**2) + 1)

=======
Suggestion 2

def main():
    # 读入数据
    r,x,y = map(int,input().split())
    # 计算距离
    distance = (x**2+y**2)**0.5
    # 计算步数
    if distance == r:
        print(1)
    elif distance <= 2*r:
        print(2)
    else:
        print(int(distance//r)+1)

=======
Suggestion 3

def main():
    r, x, y = map(int, input().split())
    if r*r == x*x + y*y:
        print(1)
    elif r*r > x*x + y*y:
        print(2)
    else:
        ans = 0
        while r*r < x*x + y*y:
            ans += 1
            r += r
        print(ans)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    r,x,y = map(int,input().split())
    if r*r == x*x + y*y:
        print(1)
    elif r*r > x*x + y*y:
        print(2)
    else:
        count = 0
        while r*r < x*x + y*y:
            x -= r
            count += 1
        print(count+1)

=======
Suggestion 6

def move(R, X, Y):
    step = 0
    while X != 0 or Y != 0:
        if X > 0 and Y > 0:
            if X > Y:
                X -= R
            else:
                Y -= R
        elif X > 0 and Y < 0:
            if X > abs(Y):
                X -= R
            else:
                Y += R
        elif X < 0 and Y > 0:
            if abs(X) > Y:
                X += R
            else:
                Y -= R
        elif X < 0 and Y < 0:
            if abs(X) > abs(Y):
                X += R
            else:
                Y += R
        elif X == 0 and Y > 0:
            Y -= R
        elif X == 0 and Y < 0:
            Y += R
        elif X > 0 and Y == 0:
            X -= R
        elif X < 0 and Y == 0:
            X += R
        else:
            break
        step += 1
    return step

=======
Suggestion 7

def problems198_c():
    pass

=======
Suggestion 8

def main():
    R, X, Y = map(int, input().split())
    if R**2 > X**2 + Y**2:
        print(2)
    else:
        print((X**2 + Y**2)**(1/2) // R + 1)

=======
Suggestion 9

def main():
    R,X,Y = map(int,input().split())
    dist = (X**2 + Y**2)**0.5
    if dist%R == 0:
        print(int(dist//R))
    else:
        print(int(dist//R)+1)

main()
