def main():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    ans = 0
    for h in range(H):
        for w in range(W):
            ans += A[h][w]
    ans = ans - H * W * min([min(A[h]) for h in range(H)])
    print(ans)
