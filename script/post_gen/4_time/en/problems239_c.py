Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x_1, y_1, x_2, y_2 = map(int, input().split())
    if (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 == 5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print("Yes")
        return
    if (x1 - y2) ** 2 + (y1 - x2) ** 2 == 5:
        print("Yes")
        return
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 0:
        print("No")
        return
    if (x1 - y2) ** 2 + (y1 - x2) ** 2 == 0:
        print("No")
        return
    print("No")

=======
Suggestion 3

def main():
    x1, y1, x2, y2 = map(int, input().split())
    print("Yes" if (x1 - x2) ** 2 + (y1 - y2) ** 2 == (x1 - y1) ** 2 == (x2 - y2) ** 2 else "No")

=======
Suggestion 4

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2)**2 + (y1 - y2)**2 == 5:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    x1, y1, x2, y2 = map(int, input().split())

    if (x1 - x2)**2 + (y1 - y2)**2 == 5:
        print("Yes")
    elif (x1 - y2)**2 + (y1 - x2)**2 == 5:
        print("Yes")
    elif (x1 - x2)**2 + (y1 - y2)**2 == 5*2:
        print("Yes")
    elif (x1 - y2)**2 + (y1 - x2)**2 == 5*2:
        print("Yes")
    elif (x1 - x2)**2 + (y1 - y2)**2 == 5*3:
        print("Yes")
    elif (x1 - y2)**2 + (y1 - x2)**2 == 5*3:
        print("Yes")
    elif (x1 - x2)**2 + (y1 - y2)**2 == 5*4:
        print("Yes")
    elif (x1 - y2)**2 + (y1 - x2)**2 == 5*4:
        print("Yes")
    elif (x1 - x2)**2 + (y1 - y2)**2 == 5*5:
        print("Yes")
    elif (x1 - y2)**2 + (y1 - x2)**2 == 5*5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def solve(x1, y1, x2, y2):
    return "Yes" if (x1-x2)**2 + (y1-y2)**2 == 5 else "No"

x1, y1, x2, y2 = map(int, input().split())
print(solve(x1, y1, x2, y2))

=======
Suggestion 7

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1-x2)**2 + (y1-y2)**2 == ((x1+y1)-(x2+y2))**2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = (x1 + x2 + y1 - y2) // 2
    y3 = (x1 + y2 - x2 + y1) // 2
    x4 = (x1 + x2 - y1 + y2) // 2
    y4 = (-x1 + x2 + y1 + y2) // 2
    if (x1 - x3) ** 2 + (y1 - y3) ** 2 == (x1 - x4) ** 2 + (y1 - y4) ** 2 and (x2 - x3) ** 2 + (y2 - y3) ** 2 == (x2 - x4) ** 2 + (y2 - y4) ** 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    x1,y1,x2,y2 = map(int,input().split())
    if (x1-x2)**2 + (y1-y2)**2 == (x1+y1)**2 or (x1-x2)**2 + (y1-y2)**2 == (x1-y1)**2 or (x1-x2)**2 + (y1-y2)**2 == (-x1-y1)**2 or (x1-x2)**2 + (y1-y2)**2 == (-x1+y1)**2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    #a = int(input())
    #b = int(input())
    #c = int(input())
    #s = input()
    x1, y1, x2, y2 = map(int, input().split())
    #l = list(map(int, input().split()))
    #n = int(input())
    #s = input()
    #s = list(input())
    #s, t = input().split()
    #n = int(input())
    #a = list(map(int, input().split()))
    #a = [int(input()) for _ in range(n)]
    #a = [list(map(int, input().split())) for _ in range(n)]
    if ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 == ((x1 - 0) ** 2 + (y1 - 0) ** 2) ** 0.5 + ((x2 - 0) ** 2 + (y2 - 0) ** 2) ** 0.5:
        print("Yes")
    else:
        print("No")
