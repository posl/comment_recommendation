def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    direction = 'E'
    for i in t:
        if i == 'S':
            if direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1
            elif direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
        elif i == 'R':
            if direction == 'E':
                direction = 'S'
            elif direction == 'W':
                direction = 'N'
            elif direction == 'N':
                direction = 'E'
            elif direction == 'S':
                direction = 'W'
    print(x, y)

if __name__ == '__main__':
    main()