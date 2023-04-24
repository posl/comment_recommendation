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
Suggestion 3

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
        elif t[i] == 'R':
            d += 1
            if d == 4:
                d = 0
    print(x, y)

=======
Suggestion 4

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
            if d == 4:
                d = 0
    print(x, y)

=======
Suggestion 5

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
            dir += 1
            if dir == 4:
                dir = 0
    print(x, y)

=======
Suggestion 6

def main():
    n = int(input())
    t = input()
    x, y = 0, 0
    for i in range(n):
        if t[i] == "S":
            y += 1
        else:
            x += 1
    print(x, y)

=======
Suggestion 7

def main():
    N = int(input())
    T = input()
    x,y = 0,0
    d = 0
    for t in T:
        if t == 'S':
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            else:
                y += 1
        else:
            d = (d+1)%4
    print(x,y)

=======
Suggestion 8

def main():
    n = int(input())
    t = input()
    ans = [0, 0]
    direction = 0
    for i in t:
        if i == 'S':
            if direction == 0:
                ans[0] += 1
            elif direction == 1:
                ans[1] -= 1
            elif direction == 2:
                ans[0] -= 1
            else:
                ans[1] += 1
        else:
            direction += 1
            if direction == 4:
                direction = 0
    print(ans[0], ans[1])
