def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            if x == 0:
                if y > 0:
                    y -= 1
                else:
                    y += 1
            elif x < 0:
                x += 1
            else:
                x -= 1
        else:
            if x == 0:
                if y > 0:
                    x += 1
                else:
                    x -= 1
            elif x < 0:
                y += 1
            else:
                y -= 1
    print(x, y)
