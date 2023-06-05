def solve():
    n, m = map(int, input().split())
    a = []
    for _ in range(m):
        k = int(input())
        a.append(list(map(int, input().split())))
    for i in range(m):
        if len(a[i]) % 2 == 1:
            print("No")
            return
    for i in range(m):
        for j in range(0, len(a[i]), 2):
            if a[i][j] != a[i][j + 1]:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    solve()