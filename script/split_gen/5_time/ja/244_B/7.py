def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            if y == 0:
                x += 1
            elif y > 0:
                y -= 1
            else:
                y += 1
        else:
            if y == 0:
                y = x
                x = 0
            elif y > 0:
                x = -y
                y = 0
            else:
                x = abs(y)
                y = 0
    print(x, y)
