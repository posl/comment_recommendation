def solve(H, W, A, B):
    if A == 0 and B == 0:
        return 1
    if A == 0:
        return solve(W, H, B, A)
    if H == 1:
        return 1
    res = 0
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if i == 0 and j == 1:
                continue
            if i == 1 and j == 0:
                continue
            if i == 1 and j == 1:
                continue
            res += solve(i, j, A-1, B) * solve(H-i, j, 0, B) + solve(i, W-j, A-1, B) * solve(H-i, W-j, 0, B) + solve(i, j, A-1, B) * solve(H-i, W-j, 0, B) + solve(i, W-j, A-1, B) * solve(H-i, j, 0, B)
    return res
H, W, A, B = map(int, input().split())
print(solve(H, W, A, B))
