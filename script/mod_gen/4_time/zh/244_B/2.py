def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    face = 0
    for i in range(n):
        if t[i] == 'S':
            if face == 0:
                x += 1
            elif face == 1:
                y -= 1
            elif face == 2:
                x -= 1
            elif face == 3:
                y += 1
        else:
            face = (face + 1) % 4
    print(x, y)

if __name__ == '__main__':
    main()