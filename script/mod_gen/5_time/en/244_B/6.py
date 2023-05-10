def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    for i in range(N):
        if T[i] == 'S':
            if i % 4 == 0:
                x += 1
            elif i % 4 == 1:
                y -= 1
            elif i % 4 == 2:
                x -= 1
            elif i % 4 == 3:
                y += 1
        elif T[i] == 'R':
            if i % 4 == 0:
                y -= 1
            elif i % 4 == 1:
                x -= 1
            elif i % 4 == 2:
                y += 1
            elif i % 4 == 3:
                x += 1
    print(str(x) + ' ' + str(y))

if __name__ == '__main__':
    main()