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
            elif direction == 90:
                y -= 1
            elif direction == 180:
                x -= 1
            elif direction == 270:
                y += 1
        elif T[i] == "R":
            direction = (direction + 90) % 360
    print(x, y)

if __name__ == '__main__':
    main()