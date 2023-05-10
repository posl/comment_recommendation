Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    d = 0
    for t in T:
        if t == 'S':
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1
        elif t == 'R':
            d = (d + 1) % 4
    print(x, y)

=======
Suggestion 2

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    for i in range(N):
        if T[i] == 'S':
            if T[i-1] == 'R':
                if y > 0:
                    y -= 1
                elif x > 0:
                    x -= 1
                elif y < 0:
                    y += 1
                else:
                    x += 1
            else:
                if x > 0:
                    x += 1
                elif y < 0:
                    y -= 1
                elif x < 0:
                    x -= 1
                else:
                    y += 1
        else:
            if x > 0:
                x -= 1
            elif y < 0:
                y += 1
            elif x < 0:
                x += 1
            else:
                y -= 1
    print(x, y)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    x = 0
    y = 0
    for i in range(n):
        if s[i] == 'S':
            if y == 0:
                x += 1
            elif y > 0:
                y -= 1
            else:
                y += 1
        else:
            if y == 0:
                y -= 1
            elif y > 0:
                y -= 1
            else:
                y += 1
    print(x, y)

=======
Suggestion 4

def solve():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
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
Suggestion 5

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
Suggestion 6

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
                if y > 0:
                    y -= 1
                elif y < 0:
                    y += 1
                else:
                    x += 1
            elif x > 0:
                x += 1
            else:
                x -= 1
        else:
            if x == 0:
                if y > 0:
                    x += 1
                elif y < 0:
                    x -= 1
                else:
                    y -= 1
            elif x > 0:
                x -= 1
            else:
                x += 1
    print(x, y)

=======
Suggestion 8

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            if y == 0:
                x += 1
            elif y > 0:
                y -= 1
            else:
                y += 1
        else:
            if y == 0:
                y = x
                x = 0
            elif y > 0:
                x = -y
                y = 0
            else:
                x = abs(y)
                y = 0
    print(x, y)

=======
Suggestion 9

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            if x == 0:
                y += 1
            elif x > 0:
                x -= 1
            elif x < 0:
                x += 1
        elif t[i] == 'R':
            if x == 0 and y == 1:
                x -= 1
            elif x == 0 and y == -1:
                x += 1
            elif x == 1 and y == 0:
                y -= 1
            elif x == -1 and y == 0:
                y += 1
    print(x, y)

=======
Suggestion 10

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    d = 0
    for t in T:
        if t == 'S':
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
main()
