def main():
    n = int(input())
    s = input()
    x = 0
    y = 0
    for i in range(n):
        if s[i] == 'S':
            if y > 0:
                y -= 1
            elif y < 0:
                y += 1
            elif x > 0:
                x -= 1
            elif x < 0:
                x += 1
        else:
            if y > 0:
                x += 1
            elif y < 0:
                x -= 1
            elif x > 0:
                y += 1
            elif x < 0:
                y -= 1
    print(x, y)
