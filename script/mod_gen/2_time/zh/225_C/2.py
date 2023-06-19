def solve():
    n, m = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(n)]
    A = [[0] * 7 for _ in range(10**2)]
    for i in range(10**2):
        for j in range(7):
            A[i][j] = (i) * 7 + j + 1
    for i in range(10**2):
        for j in range(7):
            if A[i][j] == B[0][0]:
                for k in range(n):
                    for l in range(m):
                        if i + k >= 10**2 or j + l >= 7:
                            print("No")
                            return
                        if A[i + k][j + l] != B[k][l]:
                            print("No")
                            return
                print("Yes")
                return
    print("No")
solve()
