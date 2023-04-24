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
            elif direction == 90:
                y -= 1
            elif direction == 180:
                x -= 1
            elif direction == 270:
                y += 1
        elif T[i] == "R":
            direction = (direction + 90) % 360
    print(x, y)

=======
Suggestion 2

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
        elif T[i] == "R":
            dir = (dir + 1) % 4
    print(x, y)

=======
Suggestion 4

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
            elif direction == 3:
                y += 1
        else:
            direction = (direction + 1) % 4
    print(x, y)

=======
Suggestion 5

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    dir = 0
    for i in range(n):
        if t[i] == 'S':
            if dir == 0:
                x += 1
            elif dir == 1:
                y -= 1
            elif dir == 2:
                x -= 1
            elif dir == 3:
                y += 1
        elif t[i] == 'R':
            dir = (dir + 1) % 4
    print(str(x) + " " + str(y))

=======
Suggestion 6

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    d = 0
    for i in range(N):
        if T[i] == "S":
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1
        elif T[i] == "R":
            d = (d + 1) % 4
    print(x, y)

=======
Suggestion 7

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    direction = 0
    for i in t:
        if i == 'S':
            if direction == 0:
                x += 1
            elif direction == 1:
                y -= 1
            elif direction == 2:
                x -= 1
            elif direction == 3:
                y += 1
        elif i == 'R':
            direction += 1
            if direction == 4:
                direction = 0
    print(x, y)

=======
Suggestion 8

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    face = 0
    for t in T:
        if t == 'S':
            if face == 0:
                x += 1
            elif face == 1:
                y -= 1
            elif face == 2:
                x -= 1
            elif face == 3:
                y += 1
        elif t == 'R':
            face = (face + 1) % 4
    print(x, y)

=======
Suggestion 9

def main():
    N = int(input())
    T = input()
    x = y = 0
    direction = 0
    for t in T:
        if t == 'S':
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

main()

=======
Suggestion 10

def main():
    N = int(input())
    T = input()
    S = 0
    R = 0
    for i in range(N):
        if T[i] == "S":
            S += 1
        else:
            R += 1
    x = S - R
    y = N - 2 * R
    print(x, y)
