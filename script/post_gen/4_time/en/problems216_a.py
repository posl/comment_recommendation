Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split("."))
    if y <= 2:
        print(str(x) + "-")
    elif y <= 6:
        print(x)
    else:
        print(str(x) + "+")

=======
Suggestion 2

def main():
    x, y = map(int, input().split("."))
    if y <= 2:
        print(str(x) + "-")
    elif y <= 6:
        print(str(x))
    else:
        print(str(x) + "+")

=======
Suggestion 3

def main():
    x, y = input().split(".")
    y = int(y)
    if y <= 2:
        print(x + "-")
    elif y <= 6:
        print(x)
    else:
        print(x + "+")

=======
Suggestion 4

def main():
    x, y = map(int, input().split('.'))
    if 0 <= y <= 2:
        print(str(x) + '-')
    elif 3 <= y <= 6:
        print(x)
    else:
        print(str(x) + '+')

=======
Suggestion 5

def main():
    x, y = input().split('.')
    y = int(y)
    if 0 <= y <= 2:
        print(x+'-')
    elif 3 <= y <= 6:
        print(x)
    elif 7 <= y <= 9:
        print(x+'+')

=======
Suggestion 6

def main():
    x, y = map(int, input().split('.'))
    if y <= 2:
        print(str(x) + '-')
    elif y >= 3 and y <= 6:
        print(x)
    else:
        print(str(x) + '+')

=======
Suggestion 7

def print_answer(x, y):
    if 0 <= y <= 2:
        print(str(x) + "-")
    elif 3 <= y <= 6:
        print(str(x))
    elif 7 <= y <= 9:
        print(str(x) + "+")

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    x,y = input().rstrip().split(".")
    y = int(y)
    if y <= 2:
        print(x+"-")
    elif 3 <= y <= 6:
        print(x)
    else:
        print(x+"+")

=======
Suggestion 9

def func():
    x,y = input().split(".")
    y = int(y)
    if y <= 2:
        print(int(x)+"-")
    elif y >= 7:
        print(int(x)+"+")
    else:
        print(int(x))
func()
