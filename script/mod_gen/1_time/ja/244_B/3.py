def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    d = 0
    for i in range(n):
        if t[i] == "S":
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1
        elif t[i] == "R":
            d += 1
            if d == 4:
                d = 0
    print(x, y)

if __name__ == '__main__':
    main()