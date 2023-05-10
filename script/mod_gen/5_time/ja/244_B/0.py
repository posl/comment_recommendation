def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    d = 0
    for t in T:
        if t == 'S':
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1
        elif t == 'R':
            d = (d + 1) % 4
    print(x, y)

if __name__ == '__main__':
    main()