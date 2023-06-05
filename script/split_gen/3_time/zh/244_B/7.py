def main():
    n = int(input())
    s = input()
    x = 0
    y = 0
    direction = 0
    for i in range(n):
        if s[i] == 'R':
            direction = (direction + 1) % 4
        else:
            if direction == 0:
                x += 1
            elif direction == 1:
                y -= 1
            elif direction == 2:
                x -= 1
            elif direction == 3:
                y += 1
    print(x, y)
