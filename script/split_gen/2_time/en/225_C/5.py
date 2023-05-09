def solve():
    n,m = map(int,input().split())
    b = []
    for _ in range(n):
        b.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(m):
            b[i][j] -= i*7+j+1
    for i in range(n):
        for j in range(m):
            if b[i][j] < 0:
                print("No")
                return
    print("Yes")
    return
