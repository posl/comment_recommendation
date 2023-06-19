def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == "S":
            x += 1
        else:
            y += 1
        if y == 4:
            y = 0
        if y == -1:
            y = 3
    print(x, y)

if __name__ == '__main__':
    main()