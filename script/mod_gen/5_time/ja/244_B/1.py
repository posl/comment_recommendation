def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    for i in range(N):
        if T[i] == 'S':
            if T[i-1] == 'R':
                if y > 0:
                    y -= 1
                elif x > 0:
                    x -= 1
                elif y < 0:
                    y += 1
                else:
                    x += 1
            else:
                if x > 0:
                    x += 1
                elif y < 0:
                    y -= 1
                elif x < 0:
                    x -= 1
                else:
                    y += 1
        else:
            if x > 0:
                x -= 1
            elif y < 0:
                y += 1
            elif x < 0:
                x += 1
            else:
                y -= 1
    print(x, y)

if __name__ == '__main__':
    main()