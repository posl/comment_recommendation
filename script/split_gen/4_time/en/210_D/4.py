def main():
    H, W, C = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    ans = 10**18
    for i in range(H):
        for j in range(W):
            ans = min(ans, A[i][j] + C * (i + j))
    for i in range(H):
        for j in range(W):
            ans = min(ans, A[i][j] - C * (i + j))
    print(ans)
