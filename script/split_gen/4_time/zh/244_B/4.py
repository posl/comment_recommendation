def main():
    n = int(input())
    s = input()
    x = 0
    y = 0
    direction = 0
    for i in range(n):
        if s[i] == 'S':
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
    print(x, y)
