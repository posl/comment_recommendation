Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print(y - x)

=======
Suggestion 2

def main():
    X, Y = map(int, input().split())
    if X >= Y:
        print(0)
    else:
        print(Y-X)

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if y % 10 == 0:
        print(int(y/10) - int(x/10))
    else:
        print(int(y/10) - int(x/10) + 1)

=======
Suggestion 4

def solve(x, y):
    cnt = 0
    while True:
        x += 10
        cnt += 1
        if x >= y:
            break
    return cnt

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    print(0 if x >= y else y - x)

=======
Suggestion 6

def main():
    a = input()
    a = a.split(' ')
    x = int(a[0])
    y = int(a[1])
    if x >= y:
        print(0)
    else:
        print(y-x)

=======
Suggestion 7

def solve():
    x, y = map(int, input().split())
    print(0 if x >= y else y - x)

=======
Suggestion 8

def main():
    x, y = map(int, input().split())
    print(y - x)

=======
Suggestion 9

def main():
    x,y = [int(i) for i in input().strip().split(" ")]
    if x>=y:
        print(0)
    else:
        print(int(y-x))

=======
Suggestion 10

def main():
    x,y = map(int,input().split())
    print((y-x)%10)
