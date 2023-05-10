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
            if x == 0:
                x = -y
                y = 0
            elif x > 0:
                y = -x
                x = 0
            elif x < 0:
                y = -x
                x = 0
    print(x, y)

if __name__ == '__main__':
    main()