Synthesizing 9/10 solutions

=======
Suggestion 1

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
            direction += 1
            direction %= 4
    print(x, y)

=======
Suggestion 3

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
Suggestion 4

def main():
    N = int(input())
    T = input()
    #N = 4
    #T = "SSRS"
    #N = 20
    #T = "SRSRSSRSSSRSRRRRRSRR"
    x = 0
    y = 0
    dir = "E"
    for i in range(N):
        if T[i] == "S":
            if dir == "E":
                x += 1
            elif dir == "S":
                y -= 1
            elif dir == "W":
                x -= 1
            elif dir == "N":
                y += 1
        elif T[i] == "R":
            if dir == "E":
                dir = "S"
            elif dir == "S":
                dir = "W"
            elif dir == "W":
                dir = "N"
            elif dir == "N":
                dir = "E"
    print(x, y)

=======
Suggestion 5

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
            else:
                y += 1
        else:
            d = (d + 1) % 4
    print(x, y)

=======
Suggestion 6

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
            direction = (direction + 1) % 4

    print(x, y)

=======
Suggestion 7

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    direction = "east"
    for i in range(N):
        if T[i] == "S" and direction == "east":
            x += 1
        elif T[i] == "S" and direction == "south":
            y -= 1
        elif T[i] == "S" and direction == "west":
            x -= 1
        elif T[i] == "S" and direction == "north":
            y += 1
        elif T[i] == "R" and direction == "east":
            direction = "south"
        elif T[i] == "R" and direction == "south":
            direction = "west"
        elif T[i] == "R" and direction == "west":
            direction = "north"
        elif T[i] == "R" and direction == "north":
            direction = "east"
    print(x, y)

=======
Suggestion 8

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
        else:
            direction = (direction + 1) % 4
    
    print(str(x) + " " + str(y))

=======
Suggestion 9

def main():
    N = int(input())
    T = input()
    count = 0
    for i in T:
        if i == "S":
            count += 1
    if count > N/2:
        print(N)
    else:
        print(N - 2*count)
