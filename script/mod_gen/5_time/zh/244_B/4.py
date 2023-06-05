def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            if t[i-1] == 'R':
                if t[i-2] == 'R':
                    x += 1
                else:
                    y -= 1
            else:
                x += 1
        else:
            if t[i-1] == 'R':
                if t[i-2] == 'R':
                    y += 1
                else:
                    x -= 1
            else:
                y += 1
    print(x, y)

if __name__ == '__main__':
    main()