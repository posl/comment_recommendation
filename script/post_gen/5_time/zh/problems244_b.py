Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
            d += 1
            if d == 4:
                d = 0
    print(x, y)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    x = 0
    y = 0
    for i in range(n):
        if s[i] == 'S':
            if y > 0:
                y -= 1
            elif y < 0:
                y += 1
            elif x > 0:
                x -= 1
            elif x < 0:
                x += 1
        else:
            if y > 0:
                x += 1
            elif y < 0:
                x -= 1
            elif x > 0:
                y += 1
            elif x < 0:
                y -= 1
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
            else:
                y += 1
        else:
            d = (d + 1) % 4
    print(x, y)
main()

=======
Suggestion 4

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    direction = 0
    for i in range(n):
        if t[i] == 'S':
            if direction == 0:
                x += 1
            elif direction == 1:
                y -= 1
            elif direction == 2:
                x -= 1
            elif direction == 3:
                y += 1
        else:
            direction += 1
            if direction == 4:
                direction = 0
    print(x, y)

=======
Suggestion 5

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            if t[i-1] == 'R':
                if t[i-2] == 'R':
                    x += 1
                else:
                    y -= 1
            else:
                x += 1
        else:
            if t[i-1] == 'R':
                if t[i-2] == 'R':
                    y += 1
                else:
                    x -= 1
            else:
                y += 1
    print(x, y)

=======
Suggestion 6

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
            else:
                y += 1
        else:
            d = (d + 1) % 4
    print(x, y)

=======
Suggestion 7

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
Suggestion 8

def problem244_b():
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
Suggestion 9

def main():
    n = int(input())
    t = input()
    x, y = 0, 0
    f = 0
    for i in range(n):
        if t[i] == 'S':
            if f == 0:
                x += 1
            elif f == 1:
                y -= 1
            elif f == 2:
                x -= 1
            else:
                y += 1
        else:
            f = (f + 1) % 4
    print(x, y)
