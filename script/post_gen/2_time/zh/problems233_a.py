Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x,y = map(int,input().split())
    if x >= y:
        print(0)
    else:
        print(y//10 - x//10)

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    print((y - x) // 10)

=======
Suggestion 3

def main():
    x,y = map(int,input().split())
    print((y-x%y)%y)

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print((y - x) // 10)

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        print(1 + (y - x) // 10)

=======
Suggestion 6

def solve(x,y):
    if x >= y:
        return 0
    else:
        return (y-x)/10

=======
Suggestion 7

def main():
    x,y = map(int,input().split())
    print(int((y-x)/10+0.9))
