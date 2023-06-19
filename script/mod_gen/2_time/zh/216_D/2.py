def solve():
    n,m = map(int,input().split())
    k = [int(input()) for _ in range(m)]
    a = [list(map(int,input().split())) for _ in range(m)]
    if m%2!=0:
        print("No")
        return
    for i in range(m):
        for j in range(k[i]-1):
            if a[i][j]==a[i][j+1]:
                print("No")
                return
    for i in range(1,m,2):
        if k[i]!=k[i-1]:
            print("No")
            return
        for j in range(k[i]):
            if a[i][j]!=a[i-1][j]:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    solve()