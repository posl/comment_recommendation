Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if y % 2 == 0 and y >= 2 * x and y <= 4 * x:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    x, y = map(int, input().split())

    for i in range(x+1):
        if i * 2 + (x - i) * 4 == y:
            print("Yes")
            return

    print("No")

=======
Suggestion 3

def main():
    x,y = map(int, input().split())

    if 2*x <= y <= 4*x and y % 2 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def cranes_and_turtles():
    x, y = map(int, input().split())
    if y % 2 == 0 and 2 * x <= y <= 4 * x:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    x,y = map(int,input().split())
    if (2*x<=y) and (y<=4*x) and (y%2==0):
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    X, Y = map(int, input().split())
    if Y % 2 == 0:
        if (Y/2) >= X and X >= (Y/4):
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 7

def main():
    x,y = map(int, input().split())
    if y%2 == 0 and (y/2-x) >= 0 and (y/2-x) <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def solve(X,Y):
    if Y%2 == 0:
        if 2*X <= Y <= 4*X:
            return "Yes"
        else:
            return "No"
    else:
        return "No"

X,Y = map(int,input().split())
print(solve(X,Y))

=======
Suggestion 9

def main():
    x,y = map(int,input().split())
    if y%2 == 0:
        if (y-4*x) <= 0 and (y-2*x) >= 0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 10

def main():
    legs = 0
    legs = input().split()
    X = int(legs[0])
    Y = int(legs[1])
    if X*2 <= Y and X*4 >= Y and Y%2 == 0:
        print('Yes')
    else:
        print('No')
