def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    sumA = sum(sum(a) for a in A)
    if sumA % (H*W) != 0:
        print(-1)
        return
    ave = sumA // (H*W)
    ans = 0
    for i in range(H):
        for j in range(W):
            if (i+j) % 2 == 0:
                if A[i][j] > ave:
                    ans += A[i][j] - ave
            else:
                if A[i][j] < ave:
                    ans += ave - A[i][j]
    print(ans)
