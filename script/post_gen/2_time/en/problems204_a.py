Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y = map(int, input().split())
    if x == 0:
        if y == 1:
            print(2)
        else:
            print(0)
    elif x == 1:
        if y == 2:
            print(0)
        else:
            print(1)
    else:
        if y == 0:
            print(1)
        else:
            print(2)

=======
Suggestion 2

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    elif x == 0 and y == 1:
        print(2)
    elif x == 1 and y == 2:
        print(0)
    elif x == 2 and y == 0:
        print(1)
    elif x == 1 and y == 0:
        print(2)
    elif x == 2 and y == 1:
        print(0)
    elif x == 0 and y == 2:
        print(1)
    else:
        print('error')

=======
Suggestion 3

def main():
    x, y = input().split()
    if x == y:
        print(x)
    elif x == '0' and y == '1':
        print('2')
    elif x == '1' and y == '0':
        print('2')
    elif x == '1' and y == '2':
        print('0')
    elif x == '2' and y == '1':
        print('0')
    elif x == '2' and y == '0':
        print('1')
    elif x == '0' and y == '2':
        print('1')
    else:
        print('Error')

=======
Suggestion 4

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3 - x - y)

=======
Suggestion 5

def main():
    x, y = map(int, input().split())
    print((x + 1) % 3)

=======
Suggestion 6

def main():
    x,y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3 - (x + y))

=======
Suggestion 7

def main():
    x = int(input())
    y = int(input())
    print((x + 1) % 3)
