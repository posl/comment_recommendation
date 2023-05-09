Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x < y:
        if x + 3 > y:
            print("Yes")
        else:
            print("No")
    else:
        if y + 3 > x:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if x < y:
        if x + 3 > y:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 3

def main():
    x, y = map(int, input().split())
    if x < y:
        x, y = y, x
    if x - y < 3:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    if x < y:
        if x + 3 > y:
            print('Yes')
        else:
            print('No')
    elif x > y:
        if x < y + 3:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    print('Yes' if x < y and x + 3 > y else 'No')

=======
Suggestion 6

def main():
    x, y = map(int, raw_input().split())
    print "Yes" if x + 3 > y else "No"

=======
Suggestion 7

def main():
    scores = input().split(' ')
    if int(scores[0]) > int(scores[1]):
        print('No')
    else:
        print('Yes')

=======
Suggestion 8

def main():
    X,Y = map(int,input().split())
    print('Yes' if X < Y and X+3 > Y else 'No')
