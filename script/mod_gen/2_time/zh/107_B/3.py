def main():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(list(input()))
    del_row = []
    del_col = []
    for i in range(H):
        if a[i].count("#") == 0:
            del_row.append(i)
    for j in range(W):
        flag = True
        for i in range(H):
            if a[i][j] == "#":
                flag = False
                break
        if flag:
            del_col.append(j)
    for i in range(H):
        if i not in del_row:
            for j in range(W):
                if j not in del_col:
                    print(a[i][j], end="")
            print()

if __name__ == '__main__':
    main()