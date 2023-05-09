def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    direction = 0
    for i in t:
        if i == 'S':
            if direction == 0:
                x += 1
            elif direction == 1:
                y -= 1
            elif direction == 2:
                x -= 1
            elif direction == 3:
                y += 1
        elif i == 'R':
            direction += 1
            if direction == 4:
                direction = 0
    print(x, y)
