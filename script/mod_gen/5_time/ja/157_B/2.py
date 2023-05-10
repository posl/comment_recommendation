def main():
    a = []
    for i in range(3):
        a.append(list(map(int, input().split())))
    n = int(input())
    b = []
    for i in range(n):
        b.append(int(input()))
    for i in range(3):
        for j in range(3):
            for k in range(n):
                if a[i][j] == b[k]:
                    a[i][j] = 0
    if a[0][0] == 0 and a[1][0] == 0 and a[2][0] == 0:
        print("Yes")
        exit()
    elif a[0][1] == 0 and a[1][1] == 0 and a[2][1] == 0:
        print("Yes")
        exit()
    elif a[0][2] == 0 and a[1][2] == 0 and a[2][2] == 0:
        print("Yes")
        exit()
    elif a[0][0] == 0 and a[0][1] == 0 and a[0][2] == 0:
        print("Yes")
        exit()
    elif a[1][0] == 0 and a[1][1] == 0 and a[1][2] == 0:
        print("Yes")
        exit()
    elif a[2][0] == 0 and a[2][1] == 0 and a[2][2] == 0:
        print("Yes")
        exit()
    elif a[0][0] == 0 and a[1][1] == 0 and a[2][2] == 0:
        print("Yes")
        exit()
    elif a[0][2] == 0 and a[1][1] == 0 and a[2][0] == 0:
        print("Yes")
        exit()
    else:
        print("No")
        exit()

if __name__ == '__main__':
    main()