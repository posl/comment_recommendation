def solve():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    for i in range(10**100 - N):
        for j in range(7 - M):
            if all([B[k][l] == i * 7 + j + l + 1 for k in range(N) for l in range(M)]):
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    solve()