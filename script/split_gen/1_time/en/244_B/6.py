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
