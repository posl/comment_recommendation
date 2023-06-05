def main():
    # input
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(input()))
    # process
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][j] == 'W':
                if a[j][i] != 'L':
                    print("不正确")
                    return
            elif a[i][j] == 'L':
                if a[j][i] != 'W':
                    print("不正确")
                    return
            elif a[i][j] == 'D':
                if a[j][i] != 'D':
                    print("不正确")
                    return
    print("正确")
    return

if __name__ == '__main__':
    main()