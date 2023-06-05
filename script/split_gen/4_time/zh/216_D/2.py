def solve():
    n, m = map(int, input().split())
    k = []
    a = []
    for i in range(m):
        k.append(int(input()))
        a.append(list(map(int, input().split())))
    if m == 1:
        if k[0] == 2 and a[0][0] == a[0][1]:
            print("Yes")
        else:
            print("No")
    else:
        for i in range(m):
            a[i].sort()
        a.sort()
        for i in range(m):
            if a[i][0] != a[i][1]:
                print("No")
                return
        for i in range(m - 1):
            if a[i][1] == a[i + 1][0]:
                print("No")
                return
        print("Yes")
