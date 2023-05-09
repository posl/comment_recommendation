def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    minA = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < minA:
                minA = A[i][j]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA
    print(ans)
