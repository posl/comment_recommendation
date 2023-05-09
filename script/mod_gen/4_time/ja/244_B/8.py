def main():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(0,n):
        if t[i] == "S":
            y = y + 1
        else:
            if x == 0:
                x = 1
            elif x == 1:
                x = 0
            elif x == 2:
                x = 3
            else:
                x = 2
    print(x,y)

if __name__ == '__main__':
    main()