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
            x += 1
        else:
            y += 1
            if y % 4 == 1:
                x *= -1
            elif y % 4 == 2:
                x *= -1
                y *= -1
            elif y % 4 == 3:
                y *= -1
            else:
                pass
    print(str(x)+" "+str(y))

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
        elif t[i] == 'R':
            d = (d+1)%4
    print(x, y)

main()

=======
Suggestion 3

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
            else:
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
        if t[i] == 'S':
            if dir == 0:
                x += 1
            elif dir == 1:
                y -= 1
            elif dir == 2:
                x -= 1
            elif dir == 3:
                y += 1
        else:
            dir += 1
            if dir == 4:
                dir = 0
    print(x, y)

main()

=======
Suggestion 5

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            if t[i-1] == 'R' and t[i-2] == 'R':
                if t[i-3] == 'R':
                    if t[i-4] == 'R':
                        if t[i-5] == 'R':
                            if t[i-6] == 'R':
                                if t[i-7] == 'R':
                                    if t[i-8] == 'R':
                                        if t[i-9] == 'R':
                                            if t[i-10] == 'R':
                                                if t[i-11] == 'R':
                                                    if t[i-12] == 'R':
                                                        if t[i-13] == 'R':
                                                            if t[i-14] == 'R':
                                                                if t[i-15] == 'R':
                                                                    if t[i-16] == 'R':
                                                                        if t[i-17] == 'R':
                                                                            if t[i-18] == 'R':
                                                                                if t[i-19] == 'R':
                                                                                    if t[i-20] == 'R':
                                                                                        y -= 1
                                                                                    else:
                                                                                        x += 1
                                                                                else:
                                                                                    y -= 1
                                                                            else:
                                                                                x -= 1
                                                                        else:
                                                                            y += 1
                                                                    else:
                                                                        x += 1
                                                                else:
                                                                    y -= 1
                                                            else:
                                                                x -= 1
                                                        else:
                                                            y += 1
                                                    else:
                                                        x += 1
                                                else:
                                                    y -= 1
                                            else:
                                                x -= 1
                                        else:
                                            y += 1
                                    else:
                                        x += 1
                                else:
                                    y -= 1
                            else:
                                x -= 1
                        else:
                            y += 1
                    else:
                        x += 1
                else:
                    y -= 1
            else:
                x += 1
        else:
            if t[i-1] == 'R' and t[i-2] == 'R':
                if t[i-3] == 'R':
                    if t[i-4] == 'R':
                        if t[i-5] == 'R':
                            if t[i-6

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
            d += 1
            d %= 4
    print(x, y)

=======
Suggestion 7

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == "S":
            x += 1
        else:
            y += 1
        if y == 4:
            y = 0
        if y == -1:
            y = 3
    print(x, y)

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
            else:
                y += 1
        else:
            d = (d + 1) % 4

    print(x, y)

=======
Suggestion 9

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    v = 0
    for i in range(N):
        if T[i] == "S":
            if v == 0:
                x += 1
            elif v == 1:
                y -= 1
            elif v == 2:
                x -= 1
            elif v == 3:
                y += 1
        else:
            v += 1
            v %= 4
    print(x, y)

=======
Suggestion 10

def main():
    N = int(input())
    T = input()
    x, y = 0, 0
    direction = "E"
    for t in T:
        if t == "S":
            if direction == "E":
                x += 1
            elif direction == "N":
                y += 1
            elif direction == "W":
                x -= 1
            elif direction == "S":
                y -= 1
        elif t == "R":
            if direction == "E":
                direction = "S"
            elif direction == "N":
                direction = "E"
            elif direction == "W":
                direction = "N"
            elif direction == "S":
                direction = "W"
    print(x, y)
