Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y = map(int, input().split())
    for i in range(X+1):
        for j in range(X+1):
            if i + j == X and 2*i + 4*j == Y:
                print("Yes")
                return
    print("No")

=======
Suggestion 2

def main():
    X, Y = map(int, input().split())
    if Y % 2 == 0 and 2 * X <= Y <= 4 * X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    X, Y = map(int, input().split())
    if X*2 <= Y <= X*4:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    if x*2 <= y <= x*4:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    X, Y = map(int, input().split())
    if X == 1 and Y == 2:
        print("Yes")
        return
    for i in range(1, X):
        if i * 2 + (X - i) * 4 == Y:
            print("Yes")
            return
    print("No")

=======
Suggestion 6

def main():
    X, Y = map(int, input().split())
    if X*4 < Y or Y < X*2:
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def main():
    x, y = map(int, input().split())
    if x == 1 and y == 2:
        print('Yes')
        return
    if y % 2 == 0:
        if x * 2 == y:
            print('Yes')
            return
        elif x * 4 == y:
            print('Yes')
            return
    print('No')

=======
Suggestion 8

def main():
    x, y = map(int, input().split())
    if y % 2 == 0 and x <= y//2 <= x*2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    #input
    X, Y = map(int, input().split())

    #output
    if (X*2 <= Y <= X*4):
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    x,y = map(int,input().split())
    
    if x >= 1 and x <= 100 and y >= 1 and y <= 100:
        if (y - 2*x) == 0:
            print("Yes")
        else:
            print("No")
