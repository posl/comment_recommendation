def main():
    N = int(input())
    T = input()
    x = y = 0
    for i in range(N):
        if T[i] == "S":
            y += 1
        else:
            if x == 0:
                x = y
                y = 0
            else:
                x = 0 - x
    print(x, y)

if __name__ == '__main__':
    main()