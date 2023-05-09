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

if __name__ == '__main__':
    main()