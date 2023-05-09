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
