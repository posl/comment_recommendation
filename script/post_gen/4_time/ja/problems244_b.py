Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            y += 1
        else:
            x += 1
    print(x, y)

=======
Suggestion 2

def main():
    n = int(input())
    t = input()
    x, y = 0, 0
    for i in range(n):
        if t[i] == 'S':
            y += 1
        else:
            x += 1
    print(x, y)

=======
Suggestion 3

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == "S":
            if y == 0:
                x += 1
            elif y > 0:
                y -= 1
            else:
                y += 1
        else:
            if y == 0:
                y += 1
            elif y > 0:
                y -= 1
            else:
                y += 1
    print(x,y)

=======
Suggestion 4

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            if x > 0:
                x -= 1
            elif x < 0:
                x += 1
            elif y > 0:
                y -= 1
            elif y < 0:
                y += 1
        else:
            if x > 0:
                y -= 1
            elif x < 0:
                y += 1
            elif y > 0:
                x += 1
            elif y < 0:
                x -= 1
    print(x, y)

=======
Suggestion 5

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    for i in range(N):
        if T[i] == 'S':
            if y >= 0:
                y += 1
            else:
                y -= 1
        else:
            if y >= 0:
                y -= 1
            else:
                y += 1
    print(x, y)

=======
Suggestion 6

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    for i in range(N):
        if T[i] == 'S':
            if x == 0:
                if y > 0:
                    y -= 1
                else:
                    y += 1
            elif y == 0:
                if x > 0:
                    x -= 1
                else:
                    x += 1
        else:
            if x == 0:
                if y > 0:
                    x += 1
                else:
                    x -= 1
            elif y == 0:
                if x > 0:
                    y += 1
                else:
                    y -= 1
    print(x, y)

=======
Suggestion 7

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    for i in range(N):
        if T[i] == 'S':
            if x == 0:
                y += 1
            elif x == 1:
                y -= 1
            elif x == 2:
                x -= 1
            elif x == 3:
                x += 1
        elif T[i] == 'R':
            if x == 0:
                x += 1
            elif x == 1:
                x -= 1
            elif x == 2:
                y += 1
            elif x == 3:
                y -= 1
    print(x, y)

=======
Suggestion 8

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    direction = "E"
    for i in range(N):
        if T[i] == "S":
            if direction == "E":
                x += 1
            elif direction == "S":
                y -= 1
            elif direction == "W":
                x -= 1
            elif direction == "N":
                y += 1
        else:
            if direction == "E":
                direction = "S"
            elif direction == "S":
                direction = "W"
            elif direction == "W":
                direction = "N"
            elif direction == "N":
                direction = "E"
    print(x, y)

=======
Suggestion 9

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(0,n):
        if t[i] == "S":
            y = y + 1
        else:
            if x == 0:
                x = 1
            elif x == 1:
                x = 0
            elif x == 2:
                x = 3
            else:
                x = 2
    print(x,y)

=======
Suggestion 10

def main():
    N = int(input())
    T = input()
    x, y = 0, 0
    for i in range(N):
        if T[i] == 'S':
            if x == 0:
                if y > 0:
                    y += 1
                else:
                    y -= 1
            elif x > 0:
                x += 1
            else:
                x -= 1
        else:
            if x == 0:
                if y > 0:
                    x -= 1
                else:
                    x += 1
            elif x > 0:
                x -= 1
            else:
                x += 1
    print(x, y)
