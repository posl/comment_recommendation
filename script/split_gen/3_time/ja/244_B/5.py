def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    direction = 1
    for t in T:
        if t == "S":
            if direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
            else:
                y += 1
        else:
            direction += 1
            if direction == 5:
                direction = 1
    print(x, y)
