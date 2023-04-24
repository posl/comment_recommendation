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
                y += 1
            elif direction == 2:
                x -= 1
            elif direction == 3:
                y -= 1
        elif T[i] == 'R':
            direction = (direction + 1) % 4
    print(x, y)

=======
Suggestion 3

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    direction = 'E'
    for i in range(N):
        if T[i] == 'S':
            if direction == 'E':
                x += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'W':
                x -= 1
            elif direction == 'N':
                y += 1
        elif T[i] == 'R':
            if direction == 'E':
                direction = 'S'
            elif direction == 'S':
                direction = 'W'
            elif direction == 'W':
                direction = 'N'
            elif direction == 'N':
                direction = 'E'
    print(x,y)

=======
Suggestion 4

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    direction = "east"
    for i in range(N):
        if T[i] == "S":
            if direction == "east":
                x += 1
            elif direction == "west":
                x -= 1
            elif direction == "south":
                y -= 1
            elif direction == "north":
                y += 1
        elif T[i] == "R":
            if direction == "east":
                direction = "south"
            elif direction == "west":
                direction = "north"
            elif direction == "south":
                direction = "west"
            elif direction == "north":
                direction = "east"
    print(x, y)

=======
Suggestion 5

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
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
        else:
            if direction == 4:
                direction = 1
            else:
                direction += 1
    print(x,y)

=======
Suggestion 6

def main():
    N = int(input())
    T = input()

    x = 0
    y = 0
    direction = "E"

    for i in range(N):
        if T[i] == "S":
            if direction == "E":
                x += 1
            elif direction == "W":
                x -= 1
            elif direction == "N":
                y += 1
            else:
                y -= 1
        else:
            if direction == "E":
                direction = "S"
            elif direction == "W":
                direction = "N"
            elif direction == "N":
                direction = "E"
            else:
                direction = "W"

    print(x, y)

=======
Suggestion 7

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    direction = "East"
    for i in range(N):
        if direction == "East":
            if T[i] == "S":
                x += 1
            else:
                direction = "South"
        elif direction == "South":
            if T[i] == "S":
                y -= 1
            else:
                direction = "West"
        elif direction == "West":
            if T[i] == "S":
                x -= 1
            else:
                direction = "North"
        elif direction == "North":
            if T[i] == "S":
                y += 1
            else:
                direction = "East"
    print(x, y)

=======
Suggestion 8

def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    dir = 0
    for c in T:
        if c == 'S':
            if dir == 0:
                x += 1
            elif dir == 1:
                y -= 1
            elif dir == 2:
                x -= 1
            elif dir == 3:
                y += 1
        elif c == 'R':
            dir += 1
            if dir > 3:
                dir = 0
    print(x, y)

=======
Suggestion 9

def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    d = 0 # 0:東 1:南 2:西 3:北
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
Suggestion 10

def main():
    N = int(input())
    T = input()
    #東西南北の移動をリストに
    move = []
    #東西南北の移動をリストに
    move.append([1,0])
    move.append([-1,0])
    move.append([0,-1])
    move.append([0,1])
    #向きのリストを作成
    direction = []
    #東西南北の向きをリストに
    direction.append(0)
    direction.append(1)
    direction.append(2)
    direction.append(3)
    #現在の向き
    now_direction = 0
    #現在の位置
    now_position = [0,0]
    for i in range(N):
        #Rの場合
        if T[i] == "R":
            #向きを変更
            now_direction = direction[(direction.index(now_direction) + 1) % 4]
        #Sの場合
        else:
            #移動
            now_position[0] += move[now_direction][0]
            now_position[1] += move[now_direction][1]
    print(now_position[0], now_position[1])
