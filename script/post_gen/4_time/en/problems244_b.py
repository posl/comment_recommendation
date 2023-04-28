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
            else:
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
    direction = 0
    for i in range(n):
        if t[i] == "S":
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
    print(str(x) + " " + str(y))

=======
Suggestion 3

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    dir = 0
    for i in range(N):
        if T[i] == "S":
            if dir == 0:
                x += 1
            elif dir == 1:
                y -= 1
            elif dir == 2:
                x -= 1
            elif dir == 3:
                y += 1
        else:
            dir = (dir + 1) % 4
    print(x, y)

=======
Suggestion 4

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    dir = 0
    for i in range(n):
        if t[i] == "S":
            if dir == 0:
                x += 1
            elif dir == 1:
                y -= 1
            elif dir == 2:
                x -= 1
            else:
                y += 1
        else:
            dir = (dir + 1) % 4
    print(x, y)

=======
Suggestion 5

def main():
    N = int(input())
    T = input()
    x, y = 0, 0
    direction = 0
    for t in T:
        if t == 'S':
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
Suggestion 6

def main():
    n = int(input())
    t = input()
    x, y = 0, 0
    direction = 0
    for i in range(n):
        if t[i] == 'S':
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
Suggestion 7

def main():
    N = int(input())
    T = input()
    x, y = 0, 0
    direction = 0
    for i in range(N):
        if T[i] == "S":
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
Suggestion 8

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    d = 'E'
    for i in range(N):
        if T[i] == 'S':
            if d == 'E':
                x += 1
            elif d == 'N':
                x -= 1
            elif d == 'W':
                y -= 1
            else:
                y += 1
        else:
            if d == 'E':
                d = 'S'
            elif d == 'S':
                d = 'W'
            elif d == 'W':
                d = 'N'
            else:
                d = 'E'
    print(x, y)
main()

=======
Suggestion 9

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    dir = "E"
    for i in range(n):
        if t[i] == "S":
            if dir == "E":
                x += 1
            elif dir == "S":
                y -= 1
            elif dir == "W":
                x -= 1
            else:
                y += 1
        elif t[i] == "R":
            if dir == "E":
                dir = "S"
            elif dir == "S":
                dir = "W"
            elif dir == "W":
                dir = "N"
            else:
                dir = "E"
    print(x, y)
