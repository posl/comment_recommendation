Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return False
    elif x1 == x2 and y1 != y2:
        return True
    elif x1 != x2 and y1 == y2:
        return True
    else:
        return abs(x1 - x2) == abs(y1 - y2)

=======
Suggestion 2

def solve():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 + y1) == (x2 + y2) or (x1 - y1) == (x2 - y2) or abs(x1 - x2) + abs(y1 - y2) <= 3:
        print("Yes")
    else:
        print("No")
    return 0

=======
Suggestion 3

def solve():
    x1, y1, x2, y2 = map(int, input().split())
    if abs(x1-x2)**2 + abs(y1-y2)**2 == 5:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def solve(x1,y1,x2,y2):
    if abs(x1-x2) == 5**0.5 and abs(y1-y2) == 5**0.5:
        return 'Yes'
    elif abs(x1-y2) == 5**0.5 and abs(y1-x2) == 5**0.5:
        return 'Yes'
    elif abs(x1-x2) == 5**0.5 and abs(y1-y2) == 5**0.5:
        return 'Yes'
    elif abs(x1-y2) == 5**0.5 and abs(y1-x2) == 5**0.5:
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 5

def main():
    x1,y1,x2,y2 = map(int,input().split())
    if x1 == x2 and y1 == y2:
        print("No")
    elif x1 == x2:
        print("Yes")
    elif y1 == y2:
        print("Yes")
    elif abs(x1-x2) == abs(y1-y2):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print('Yes')
        return
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 8:
        print('Yes')
        return
    print('No')

main()

=======
Suggestion 7

def main():
    x1, y1, x2, y2 = map(int, input().split())

    if (x1, y1) == (x2, y2):
        print('No')
        return

    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print('Yes')
        return

    if (x1 + y1) == (x2 + y2) or (x1 - y1) == (x2 - y2):
        print('Yes')
        return

    print('No')
    return

=======
Suggestion 8

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1-x2)**2 + (y1-y2)**2 == 5:
        print("Yes")
        return
    if (x1-x2)**2 + (y1-y2)**2 == 50:
        print("Yes")
        return
    if (x1-x2)**2 + (y1-y2)**2 == 25:
        print("Yes")
        return
    print("No")
    return

=======
Suggestion 9

def main():
    # input
    x1,y1,x2,y2 = map(int, input().split())

    # compute
    if (x1+x2+y1+y2)%2 == 0:
        if abs(x1-x2) == abs(y1-y2):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 10

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print('Yes')
        return
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 10:
        print('Yes')
        return
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 25:
        print('Yes')
        return
    print('No')
    return
