def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    v = 0
    for i in range(N):
        if T[i] == "S":
            if v == 0:
                x += 1
            elif v == 1:
                y -= 1
            elif v == 2:
                x -= 1
            elif v == 3:
                y += 1
        else:
            v += 1
            v %= 4
    print(x, y)

if __name__ == '__main__':
    main()