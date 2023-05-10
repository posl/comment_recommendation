def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            if x == 0:
                y += 1
            elif x == 1:
                x -= 1
            elif x == -1:
                x += 1
            elif y == 0:
                x += 1
            elif y == 1:
                y -= 1
            elif y == -1:
                y += 1
        elif t[i] == 'R':
            if x == 0:
                x += 1
            elif x == 1:
                y -= 1
            elif x == -1:
                y += 1
            elif y == 0:
                x -= 1
            elif y == 1:
                y += 1
            elif y == -1:
                y -= 1
    print(x, y)
