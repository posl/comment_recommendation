Synthesizing 10/10 solutions

=======
Suggestion 1

def problems244_b():
    n = int(input())
    t = input()
    x = 0
    y = 0
    flag = 1
    for i in range(n):
        if t[i] == 'S':
            if flag == 1:
                x += 1
            elif flag == 2:
                y -= 1
            elif flag == 3:
                x -= 1
            elif flag == 4:
                y += 1
        elif t[i] == 'R':
            flag = (flag%4)+1
    print(x,y)

=======
Suggestion 2

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    for t in T:
        if t == 'S':
            x += 1
        else:
            y += 1
    print(x, y)

=======
Suggestion 3

def main():
    # input
    n = int(input())
    t = input()
    # init
    x = 0
    y = 0
    # loop
    for i in range(n):
        if t[i] == 'S':
            if y == 0:
                x += 1
            elif y > 0:
                y -= 1
            elif y < 0:
                y += 1
        elif t[i] == 'R':
            if y == 0:
                y -= x
                x = 0
            elif y > 0:
                x += y
                y = 0
            elif y < 0:
                x -= y
                y = 0
    # output
    print(x, y)
    return

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    x = 0
    y = 0
    d = 0
    for i in range(n):
        if s[i] == "S":
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1
        elif s[i] == "R":
            d += 1
            if d == 4:
                d = 0
    print(x, y)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    x = 0
    y = 0
    for i in range(n):
        if s[i] == 'S':
            if x == 0:
                y += 1
            elif x == 1:
                x -= 1
            elif x == 2:
                y -= 1
            else:
                x += 1
        else:
            x += 1
            if x > 3:
                x = 0
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
        if t[i] == "S":
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
Suggestion 8

def main():
    n = int(input())
    s = input()
    x = 0
    y = 0
    direction = 0
    for i in range(n):
        if s[i] == 'R':
            direction = (direction + 1) % 4
        else:
            if direction == 0:
                x += 1
            elif direction == 1:
                y -= 1
            elif direction == 2:
                x -= 1
            elif direction == 3:
                y += 1
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
            if t[i - 1] == 'R':
                if t[i - 2] == 'R':
                    x = x - 1
                else:
                    y = y - 1
            else:
                x = x + 1
        else:
            if t[i - 1] == 'S':
                if t[i - 2] == 'S':
                    x = x - 1
                else:
                    y = y - 1
            else:
                x = x + 1
    print(x, y)

=======
Suggestion 10

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
            d += 1
            if d == 4:
                d = 0
    print(x, y)
main()
