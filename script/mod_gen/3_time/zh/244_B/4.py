def main():
    n = int(input())
    s = input()
    x = 0
    y = 0
    for i in range(n):
        if s[i] == 'S':
            if x == 0:
                y += 1
            elif x == 1:
                x -= 1
            elif x == 2:
                y -= 1
            else:
                x += 1
        else:
            x += 1
            if x > 3:
                x = 0
    print(x, y)

if __name__ == '__main__':
    main()