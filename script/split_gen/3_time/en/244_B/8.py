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
