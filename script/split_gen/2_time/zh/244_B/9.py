def main():
    N = int(input())
    T = input()
    x, y = 0, 0
    direction = "E"
    for t in T:
        if t == "S":
            if direction == "E":
                x += 1
            elif direction == "N":
                y += 1
            elif direction == "W":
                x -= 1
            elif direction == "S":
                y -= 1
        elif t == "R":
            if direction == "E":
                direction = "S"
            elif direction == "N":
                direction = "E"
            elif direction == "W":
                direction = "N"
            elif direction == "S":
                direction = "W"
    print(x, y)
