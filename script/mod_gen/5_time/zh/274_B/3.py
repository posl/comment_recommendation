def solve():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                ans[i][j] = "#"
    for i in range(H):
        print("".join(ans[i]))

if __name__ == '__main__':
    solve()