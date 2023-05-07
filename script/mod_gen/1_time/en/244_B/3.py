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

if __name__ == '__main__':
    main()