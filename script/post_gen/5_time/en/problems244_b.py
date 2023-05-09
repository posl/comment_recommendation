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
            if x == 0:
                y += 1
            elif x == 1:
                x -= 1
            elif x == -1:
                x += 1
            elif y == 0:
                x += 1
            elif y == 1:
                y -= 1
            elif y == -1:
                y += 1
        elif t[i] == 'R':
            if x == 0:
                x += 1
            elif x == 1:
                y -= 1
            elif x == -1:
                y += 1
            elif y == 0:
                x -= 1
            elif y == 1:
                y += 1
            elif y == -1:
                y -= 1
    print(x, y)

=======
Suggestion 2

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
            if x == 0:
                x = -y
                y = 0
            elif x > 0:
                y = -x
                x = 0
            elif x < 0:
                y = -x
                x = 0
    print(x, y)

=======
Suggestion 3

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
            elif x > 0:
                x -= 1
            elif x < 0:
                x += 1
        elif T[i] == 'R':
            if x == 0:
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
Suggestion 4

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            if x == 0:
                if y > 0:
                    y -= 1
                else:
                    y += 1
            elif x < 0:
                x += 1
            else:
                x -= 1
        else:
            if x == 0:
                if y > 0:
                    x += 1
                else:
                    x -= 1
            elif x < 0:
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
    for c in s:
        if c == 'S':
            x += 1
        else:
            y += 1
    print(x, y)

=======
Suggestion 6

def solve():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            y += 1
        else:
            y -= 1
            if t[i] == 'R':
                x *= -1
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
            if i % 4 == 0:
                x += 1
            elif i % 4 == 1:
                y -= 1
            elif i % 4 == 2:
                x -= 1
            elif i % 4 == 3:
                y += 1
        elif T[i] == 'R':
            if i % 4 == 0:
                y -= 1
            elif i % 4 == 1:
                x -= 1
            elif i % 4 == 2:
                y += 1
            elif i % 4 == 3:
                x += 1
    print(str(x) + ' ' + str(y))

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    x, y = 0, 0
    for i in range(n):
        if s[i] == 'S':
            if y > 0:
                y -= 1
        else:
            if x == 0:
                if y > 0:
                    y -= 1
                    x += 1
                else:
                    y += 1
            else:
                if y < 0:
                    y += 1
                    x -= 1
                else:
                    y -= 1
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
        if s[i] == 'R':
            d = (d + 1) % 4
        else:
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            else:
                y += 1
    print(x, y)

=======
Suggestion 10

def main():
    # Get input here
    N = int(input())
    T = input()

    # Calculate result here
    x = 0
    y = 0
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
        elif t == 'R':
            direction += 1
            direction %= 4

    # Print output here
    print(x, y)

main()
