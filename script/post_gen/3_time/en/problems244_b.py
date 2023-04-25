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
            elif direction == 3:
                y += 1
        elif T[i] == "R":
            direction += 1
            if direction == 4:
                direction = 0
    print(str(x) + " " + str(y))

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
            elif dir == 3:
                y += 1
        elif T[i] == 'R':
            dir = (dir + 1) % 4
    print(x, y)

=======
Suggestion 3

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
        elif t[i] == 'R':
            direction = (direction + 1) % 4
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
        if t[i] == "S":
            if direction == 0:
                x += 1
            elif direction == 1:
                y -= 1
            elif direction == 2:
                x -= 1
            elif direction == 3:
                y += 1
        elif t[i] == "R":
            direction += 1
            if direction == 4:
                direction = 0
    print(x, y)

=======
Suggestion 5

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    direction = "east"
    for i in range(N):
        if direction == "east":
            if T[i] == "S":
                x += 1
            elif T[i] == "R":
                direction = "south"
        elif direction == "south":
            if T[i] == "S":
                y -= 1
            elif T[i] == "R":
                direction = "west"
        elif direction == "west":
            if T[i] == "S":
                x -= 1
            elif T[i] == "R":
                direction = "north"
        elif direction == "north":
            if T[i] == "S":
                y += 1
            elif T[i] == "R":
                direction = "east"
    print(x, y)

=======
Suggestion 6

def main():
    N = int(input())
    T = input()

    x = 0
    y = 0
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

main()

=======
Suggestion 7

def main():
    N = int(input())
    T = input()
    x, y = 0, 0
    direction = 1
    for i in range(N):
        if T[i] == "S":
            if direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
            elif direction == 4:
                y += 1
        elif T[i] == "R":
            direction += 1
            if direction == 5:
                direction = 1
    print(x, y)

=======
Suggestion 8

def main():
    N = int(input())
    T = input()
    
    #N = 20
    #T = "SRSRSSRSSSRSRRRRRSRR"
    
    x = 0
    y = 0
    # 0: East, 1: South, 2: West, 3: North
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
Suggestion 9

def main():
    N = int(input())
    T = input()
    x, y = 0, 0
    direc = "E"
    for i in range(N):
        if T[i] == "S":
            if direc == "E":
                x += 1
            elif direc == "S":
                y -= 1
            elif direc == "W":
                x -= 1
            else:
                y += 1
        else:
            if direc == "E":
                direc = "S"
            elif direc == "S":
                direc = "W"
            elif direc == "W":
                direc = "N"
            else:
                direc = "E"
    print(x, y)

=======
Suggestion 10

def move (x, y, dir):
    if dir == 'e':
        return (x + 1, y)
    elif dir == 'w':
        return (x - 1, y)
    elif dir == 'n':
        return (x, y + 1)
    elif dir == 's':
        return (x, y - 1)
    else:
        print('Error: Invalid direction')
        return (x, y)
