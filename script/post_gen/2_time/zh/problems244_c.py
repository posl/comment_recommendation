Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    T = input()
    x = y = 0
    for i in range(N):
        if T[i] == "S":
            y += 1
        else:
            if x == 0:
                x = y
                y = 0
            else:
                x = 0 - x
    print(x, y)

=======
Suggestion 2

def problem244_b():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            x += 1
        else:
            if x % 2 == 0:
                y += 1
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
    d = 0
    for i in range(n):
        if s[i] == 'S':
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
Suggestion 4

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
            direction = (direction + 1) % 4
    print(x, y)

=======
Suggestion 5

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    d = 'E'
    for i in range(n):
        if t[i] == 'S':
            if d == 'E':
                x += 1
            elif d == 'W':
                x -= 1
            elif d == 'N':
                y += 1
            else:
                y -= 1
        else:
            if d == 'E':
                d = 'S'
            elif d == 'W':
                d = 'N'
            elif d == 'N':
                d = 'W'
            else:
                d = 'E'
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
Suggestion 7

def main():
    # 输入数据
    n = int(input())
    t = input()

    # 初始化
    x = 0
    y = 0
    direction = 0

    # 处理数据
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
            direction += 1
            if direction == 4:
                direction = 0

    # 输出结果
    print(x, y)

=======
Suggestion 8

def direction_change(direction):
    if direction == 'N':
        return 'E'
    elif direction == 'E':
        return 'S'
    elif direction == 'S':
        return 'W'
    elif direction == 'W':
        return 'N'

=======
Suggestion 9

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
            d = (d + 1) % 4
    print(x, y)
