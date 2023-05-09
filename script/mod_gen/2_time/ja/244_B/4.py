def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    direction = 1
    for i in range(N):
        if T[i] == "S":
            if direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
            elif direction == 4:
                y += 1
        else:
            if direction == 4:
                direction = 1
            else:
                direction += 1
    print(x,y)

if __name__ == '__main__':
    main()