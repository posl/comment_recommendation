Synthesizing 10/10 solutions (Duplicates hidden)

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
    x, y = map(int, input().split())
    print(max(0, y - x))

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    print((y - x % y) % y)

=======
Suggestion 4

def main():
    X, Y = map(int, input().split())
    print((Y - X) // 10)

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    print((y-x)%10)

=======
Suggestion 6

def solve():
    x,y = map(int, input().split())
    print(y-x if y>x else 0)

solve()

=======
Suggestion 7

def solve():
    X,Y = map(int,input().split())
    print((Y-X)%10)
