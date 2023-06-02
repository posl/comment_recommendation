Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(x, y):
    if x >= y:
        return 0
    else:
        return (y - x) // 10 + (1 if (y - x) % 10 > 0 else 0)

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print((y-x)//10)

=======
Suggestion 3

def main():
    x,y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print(int((y-x)/10))

=======
Suggestion 4

def main():
    x,y = map(int,input().split())
    a = y - x
    if a % 10 == 0:
        print(a // 10)
    else:
        print(a // 10 + 1)

=======
Suggestion 5

def main():
    X, Y = map(int, input().split())
    print((Y - X) // 10)

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    print((y - x) // 10)

=======
Suggestion 7

def main():
    X, Y = map(int, input().split())
    print((Y-X%Y)%Y)
