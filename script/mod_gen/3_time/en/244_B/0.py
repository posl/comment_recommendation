def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    direction = 0
    for i in range(N):
        if T[i] == "S":
            if direction == 0:
                x += 1
            elif direction == 1:
                y -= 1
            elif direction == 2:
                x -= 1
            elif direction == 3:
                y += 1
        elif T[i] == "R":
            direction += 1
            if direction == 4:
                direction = 0
    print(str(x) + " " + str(y))

if __name__ == '__main__':
    main()