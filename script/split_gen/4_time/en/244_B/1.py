def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    direction = 0
    for i in range(n):
        if t[i] == "S":
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
    print(str(x) + " " + str(y))
