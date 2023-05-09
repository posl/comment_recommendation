def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    dir = "E"
    for i in range(n):
        if t[i] == "S":
            if dir == "E":
                x += 1
            elif dir == "S":
                y -= 1
            elif dir == "W":
                x -= 1
            else:
                y += 1
        elif t[i] == "R":
            if dir == "E":
                dir = "S"
            elif dir == "S":
                dir = "W"
            elif dir == "W":
                dir = "N"
            else:
                dir = "E"
    print(x, y)

if __name__ == '__main__':
    main()