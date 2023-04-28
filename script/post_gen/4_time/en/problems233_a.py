Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print(y-x)

=======
Suggestion 2

def main():
    X,Y = map(int,input().split())
    if X >= Y:
        print(0)
    else:
        print(Y-X)

=======
Suggestion 3

def main():
    x,y = map(int, input().split())
    if x < y:
        print(y-x)
    else:
        print(0)

=======
Suggestion 4

def main():
    # input
    X, Y = map(int, input().split())

    # compute

    # output
    print(0 if X >= Y else Y - X)

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    print((y - x) if y - x >= 0 else 0)

=======
Suggestion 6

def main():
    X,Y = map(int, input().split())
    ans = (Y - X) % 10
    if ans == 0:
        ans = 0
    elif ans == 1:
        ans = 1
    elif ans == 2:
        ans = 2
    elif ans == 3:
        ans = 3
    elif ans == 4:
        ans = 4
    elif ans == 5:
        ans = 5
    elif ans == 6:
        ans = 6
    elif ans == 7:
        ans = 7
    elif ans == 8:
        ans = 8
    elif ans == 9:
        ans = 9
    print(ans)

=======
Suggestion 7

def main():
    X, Y = map(int, input().split())
    print((Y-X)%10)

=======
Suggestion 8

def main():
    X,Y = map(int, input().split())
    print(int((Y-X)/10))

=======
Suggestion 9

def solve(x, y):
    return max(0, y - x)

=======
Suggestion 10

def main():
    X,Y = map(int, input().split())
    print((Y-X)%10)
    return
