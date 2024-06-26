def main():
    H, W, C = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(H)]
    ans = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    ans = min(ans, A[i][j] + A[k][l] + C*abs(i-k) + C*abs(j-l))
    print(ans)
