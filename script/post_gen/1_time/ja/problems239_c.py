Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 + y1) % 2 == (x2 + y2) % 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0:
        print("Yes")
    elif dy == 0:
        print("Yes")
    elif abs(dx) == abs(dy):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0:
        print("Yes")
    elif dy == 0:
        print("Yes")
    elif dx == dy:
        print("Yes")
    elif dx == -dy:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    x1, y1, x2, y2 = map(int, input().split())
    #x1, y1, x2, y2 = 0, 0, 3, 3
    #x1, y1, x2, y2 = 0, 1, 2, 3
    #x1, y1, x2, y2 = 1000000000, 1000000000, 999999999, 999999999

    x = x2 - x1
    y = y2 - y1

    if x == 0 and y == 0:
        print("No")
    elif x == 0 or y == 0:
        print("Yes")
    elif x == y or x == -y:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2:
        print('Yes')
        return
    elif y1 == y2:
        print('Yes')
        return
    elif abs(x1 - x2) == abs(y1 - y2):
        print('Yes')
        return
    else:
        print('No')
        return

=======
Suggestion 6

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3 = x2 - x1, y2 - y1
    x4, y4 = -y3, x3
    x5, y5 = x4 + x1, y4 + y1
    print('Yes' if x5 != x1 or y5 != y1 else 'No')

main()

=======
Suggestion 7

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x = x2 - x1
    y = y2 - y1
    if x == y:
        print("Yes")
    elif x == -y:
        print("Yes")
    elif x == 0 and y % 2 == 0:
        print("Yes")
    elif y == 0 and x % 2 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    x1,y1,x2,y2=map(int,input().split())
    if abs(x1-x2)%2==0 and abs(y1-y2)%2==0:
        print("Yes")
    elif abs(x1-x2)%2==1 and abs(y1-y2)%2==1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    x1,y1,x2,y2=map(int,input().split())
    if x1==x2:
        print("Yes")
        exit()
    if y1==y2:
        print("Yes")
        exit()
    if abs(x1-x2)==abs(y1-y2):
        print("Yes")
        exit()
    print("No")

=======
Suggestion 10

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == y1 and x2 == y2:
        print("No")
        return
    if x1 == x2 and y1 == y2:
        print("Yes")
        return
    if x1 == y1 or x2 == y2:
        print("No")
        return
    if x1 == y2 or x2 == y1:
        print("No")
        return
    print("Yes")
