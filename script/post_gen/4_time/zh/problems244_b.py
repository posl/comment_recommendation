Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    direction = 0
    for i in range(N):
        if T[i] == 'S':
            if direction == 0:
                x += 1
            elif direction == 1:
                y -= 1
            elif direction == 2:
                x -= 1
            elif direction == 3:
                y += 1
        else:
            direction = (direction + 1) % 4
    print(x, y)

=======
Suggestion 2

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    d = 0
    for i in range(n):
        if t[i] == 'S':
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1
        else:
            d = (d + 1) % 4
    print(x, y)

=======
Suggestion 3

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    face = 0
    for i in range(n):
        if t[i] == 'S':
            if face == 0:
                x += 1
            elif face == 1:
                y -= 1
            elif face == 2:
                x -= 1
            elif face == 3:
                y += 1
        else:
            face = (face + 1) % 4
    print(x, y)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    x = 0
    y = 0
    for i in range(n):
        if s[i] == 'S':
            x += 1
        else:
            if x % 2 == 0:
                y += 1
            else:
                y -= 1
    print(x, y)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    x = 0
    y = 0
    direction = 0
    for i in range(n):
        if s[i] == 'S':
            if direction == 0:
                x += 1
            elif direction == 1:
                y -= 1
            elif direction == 2:
                x -= 1
            else:
                y += 1
        else:
            direction = (direction + 1) % 4
    print(x, y)

=======
Suggestion 6

def main():
    n = int(input())
    t = input()
    x, y = 0, 0
    d = 0
    for i in range(n):
        if t[i] == 'S':
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1
        elif t[i] == 'R':
            d = (d + 1) % 4
    print(x, y)

=======
Suggestion 7

def main():
    n=int(input())
    s=input()
    x=0
    y=0
    direction='E'
    for i in range(n):
        if s[i]=='S':
            if direction=='E':
                x+=1
            elif direction=='W':
                x-=1
            elif direction=='N':
                y+=1
            elif direction=='S':
                y-=1
        elif s[i]=='R':
            if direction=='E':
                direction='S'
            elif direction=='W':
                direction='N'
            elif direction=='N':
                direction='E'
            elif direction=='S':
                direction='W'
    print(x,y)

=======
Suggestion 8

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    d = 0
    for i in range(n):
        if t[i] == "S":
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1
        elif t[i] == "R":
            d += 1
            if d > 3:
                d = 0
    print(x, y)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    x = 0
    y = 0
    d = 0
    for i in range(n):
        if s[i] == 'S':
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1
        else:
            d = (d + 1) % 4
    print(x, y)
