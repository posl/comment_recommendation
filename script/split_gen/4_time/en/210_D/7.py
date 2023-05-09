def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    minA = min([min(a) for a in A])
    minA_i, minA_j = 0, 0
    for i in range(H):
        for j in range(W):
            if A[i][j] == minA:
                minA_i, minA_j = i, j
    ans = 10**18
    for i in range(H):
        for j in range(W):
            ans = min(ans, A[i][j] + C * (abs(i - minA_i) + abs(j - minA_j)))
    print(ans)
