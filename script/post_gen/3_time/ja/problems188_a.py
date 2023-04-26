Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x < y:
        x, y = y, x
    if x - y < 3:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if abs(x - y) < 3:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if x > y:
        if x - y <= 2:
            print("Yes")
        else:
            print("No")
    else:
        if y - x <= 2:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    if abs(x - y) < 3:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    if abs(x - y) <= 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    x, y = map(int, input().split())
    print('Yes' if x + 3 > y else 'No')

=======
Suggestion 7

def calc(x,y):
    if x > y:
        if x - y == 2:
            return 'Yes'
        else:
            return 'No'
    else:
        if y - x == 2:
            return 'Yes'
        else:
            return 'No'

=======
Suggestion 8

def solve(x,y):
    if x<y:
        return "Yes"
    else:
        return "No"
