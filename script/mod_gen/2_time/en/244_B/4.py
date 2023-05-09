def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    dir = 0
    for i in range(n):
        if t[i] == 'S':
            if dir == 0:
                x += 1
            elif dir == 1:
                y -= 1
            elif dir == 2:
                x -= 1
            elif dir == 3:
                y += 1
        elif t[i] == 'R':
            dir = (dir + 1) % 4
    print(str(x) + " " + str(y))

if __name__ == '__main__':
    main()