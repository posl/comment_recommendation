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
