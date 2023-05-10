Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X,Y = map(int, input().split())
    if X >= Y:
        print(0)
    else:
        print((Y - X) // 10)

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print(int((y - x) / 10))

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print((y-x)//10)

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    print(0 if x >= y else (y - x) // 10)

=======
Suggestion 5

def solve():
    x, y = map(int, input().split())
    print(0 if x >= y else (y - x + 9) // 10)

=======
Suggestion 6

def solve():
    x,y = map(int,input().split())
    if x >= y:
        print(0)
    else:
        print((y-x)//10)

=======
Suggestion 7

def main():
    X,Y = map(int, input().split())
    ans = 0
    if X >= Y:
        ans = 0
    else:
        ans = Y // 10 - X // 10
        if Y % 10 == 0:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    x, y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print(1 + (y - x) // 10)
