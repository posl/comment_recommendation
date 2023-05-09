def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    d = 'E'
    for i in range(N):
        if T[i] == 'S':
            if d == 'E':
                x += 1
            elif d == 'N':
                x -= 1
            elif d == 'W':
                y -= 1
            else:
                y += 1
        else:
            if d == 'E':
                d = 'S'
            elif d == 'S':
                d = 'W'
            elif d == 'W':
                d = 'N'
            else:
                d = 'E'
    print(x, y)
main()

if __name__ == '__main__':
    main()