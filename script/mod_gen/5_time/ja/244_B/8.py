def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            if x == 0:
                y += 1
            elif x > 0:
                x -= 1
            elif x < 0:
                x += 1
        elif t[i] == 'R':
            if x == 0 and y == 1:
                x -= 1
            elif x == 0 and y == -1:
                x += 1
            elif x == 1 and y == 0:
                y -= 1
            elif x == -1 and y == 0:
                y += 1
    print(x, y)

if __name__ == '__main__':
    main()