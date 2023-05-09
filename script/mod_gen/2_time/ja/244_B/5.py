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

if __name__ == '__main__':
    main()