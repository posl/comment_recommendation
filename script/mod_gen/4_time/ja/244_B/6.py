def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    for i in range(N):
        if T[i] == 'S':
            if x == 0:
                y += 1
            elif x == 1:
                y -= 1
            elif x == 2:
                x -= 1
            elif x == 3:
                x += 1
        elif T[i] == 'R':
            if x == 0:
                x += 1
            elif x == 1:
                x -= 1
            elif x == 2:
                y += 1
            elif x == 3:
                y -= 1
    print(x, y)

if __name__ == '__main__':
    main()