def main():
    N = int(input())
    T = input()
    x, y = 0, 0
    direction = 1
    for i in range(N):
        if T[i] == "S":
            if direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
            elif direction == 4:
                y += 1
        elif T[i] == "R":
            direction += 1
            if direction == 5:
                direction = 1
    print(x, y)
