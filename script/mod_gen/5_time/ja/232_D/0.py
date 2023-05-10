def solve():
    H, W = map(int, input().split())
    C = []
    for _ in range(H):
        C.append(input())
    ans = 1
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if C[i][j] == "#":
                continue
            if i == 0:
                ans += 1
                continue
            if j == 0:
                ans += 1
                continue
            if C[i-1][j] == "#" and C[i][j-1] == "#":
                continue
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()