def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            x += 1
        else:
            y += 1
            if y % 4 == 1:
                x *= -1
            elif y % 4 == 2:
                x *= -1
                y *= -1
            elif y % 4 == 3:
                y *= -1
            else:
                pass
    print(str(x)+" "+str(y))
