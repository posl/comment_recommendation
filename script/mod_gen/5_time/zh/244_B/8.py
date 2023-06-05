def main():
    n = int(input())
    t = input()
    x, y = 0, 0
    f = 0
    for i in range(n):
        if t[i] == 'S':
            if f == 0:
                x += 1
            elif f == 1:
                y -= 1
            elif f == 2:
                x -= 1
            else:
                y += 1
        else:
            f = (f + 1) % 4
    print(x, y)

if __name__ == '__main__':
    main()