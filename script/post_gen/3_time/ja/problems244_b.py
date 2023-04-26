Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    direction = 0
    for i in range(N):
        if T[i] == "S":
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
    N = int(input())
    T = input()
    x = 0
    y = 0
    dir = 0
    for i in range(N):
        if T[i] == 'S':
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
Suggestion 3

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
            elif direction == "W":
                x -= 1
            elif direction == "N":
                y += 1
            elif direction == "S":
                y -= 1
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
Suggestion 4

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    direction = 'E'
    for i in range(N):
        if T[i] == 'S':
            if direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1
            elif direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
        if T[i] == 'R':
            if direction == 'E':
                direction = 'S'
            elif direction == 'S':
                direction = 'W'
            elif direction == 'W':
                direction = 'N'
            elif direction == 'N':
                direction = 'E'
    print(x,y)

=======
Suggestion 5

def main():
    N = int(input())
    T = input()

    x = 0
    y = 0
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
        elif T[i] == "R":
            direction += 1
            if direction == 4:
                direction = 0
    print(x, y)

=======
Suggestion 6

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    direction = 1
    for t in T:
        if t == "S":
            if direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
            else:
                y += 1
        else:
            direction += 1
            if direction == 5:
                direction = 1
    print(x, y)

=======
Suggestion 7

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    direction = 'E'
    for i in t:
        if i == 'S':
            if direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1
            elif direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
        elif i == 'R':
            if direction == 'E':
                direction = 'S'
            elif direction == 'W':
                direction = 'N'
            elif direction == 'N':
                direction = 'E'
            elif direction == 'S':
                direction = 'W'
    print(x, y)

=======
Suggestion 8

def main():
    N = int(input())
    T = input()

    x, y = 0, 0
    direction = 0
    for t in T:
        if t == "S":
            if direction == 0:
                x += 1
            elif direction == 1:
                y -= 1
            elif direction == 2:
                x -= 1
            elif direction == 3:
                y += 1
        elif t == "R":
            direction = (direction + 1) % 4

    print(x, y)

=======
Suggestion 9

def main():
    N = int(input())
    T = input()
    #print(N)
    #print(T)

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
        elif T[i] == 'R':
            direction += 1
            if direction == 4:
                direction = 0

    print(x, y)

=======
Suggestion 10

def main():
    N = int(input())
    T = input()
    #print(N, T)
    x = 0
    y = 0
    #東西南北の順に入れておく
    #東を向いているときは1
    #南を向いているときは2
    #西を向いているときは3
    #北を向いているときは4
    direction = 1
    for i in range(N):
        if T[i] == 'S':
            if direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
            elif direction == 4:
                y += 1
        elif T[i] == 'R':
            if direction == 4:
                direction = 1
            else:
                direction += 1
    print(x, y)
