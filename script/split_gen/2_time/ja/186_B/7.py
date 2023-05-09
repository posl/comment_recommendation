def main():
    H,W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    minA = A[0][0]
    for i in range(H):
        for j in range(W):
            minA = min(minA, A[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA
    print(ans)
