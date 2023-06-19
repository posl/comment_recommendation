def solve():
    n,m = map(int, input().split())
    b = []
    for i in range(n):
        b.append(list(map(int, input().split())))
    for i in range(1, n):
        for j in range(1, m):
            if b[i][j] - b[i][j-1] != b[i-1][j] - b[i-1][j-1]:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    solve()