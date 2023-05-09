def main():
    a = []
    for i in range(3):
        a.append(list(map(int, input().split())))
    n = int(input())
    b = []
    for i in range(n):
        b.append(int(input()))
    for i in range(n):
        for j in range(3):
            for k in range(3):
                if a[j][k] == b[i]:
                    a[j][k] = 0
    for i in range(3):
        if a[i][0] == a[i][1] == a[i][2] == 0:
            print("Yes")
            return
        elif a[0][i] == a[1][i] == a[2][i] == 0:
            print("Yes")
            return
    if a[0][0] == a[1][1] == a[2][2] == 0:
        print("Yes")
        return
    elif a[0][2] == a[1][1] == a[2][0] == 0:
        print("Yes")
        return
    print("No")
main()

if __name__ == '__main__':
    main()