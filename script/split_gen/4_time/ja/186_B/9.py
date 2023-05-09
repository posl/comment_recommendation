def get_ints(): return map(int, input().split())
H, W = get_ints()
A = [list(get_ints()) for _ in range(H)]
min_block = 101
for i in range(H):
    for j in range(W):
        min_block = min(min_block, A[i][j])
ans = 0
for i in range(H):
    for j in range(W):
        ans += (A[i][j] - min_block)
print(ans)
