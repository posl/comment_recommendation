def main():
    N = int(input())
    T = input()
    x, y = 0, 0
    direction = 0
    for t in T:
        if t == "S":
            if direction == 0:
                x += 1
            elif direction == 1:
                y -= 1
            elif direction == 2:
                x -= 1
            elif direction == 3:
                y += 1
        elif t == "R":
            direction = (direction + 1) % 4
    print(x, y)
