def main():
    # input
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    # compute
    minA = 101
    for i in range(H):
        for j in range(W):
            minA = min(minA, A[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA
    # output
    print(ans)
