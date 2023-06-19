def main():
    H, W, C = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(H)]
    ans = float('inf')
    # 从左到右，从上到下遍历
    for i in range(H):
        for j in range(W):
            # 从左到右，从上到下遍历
            for k in range(i, H):
                for l in range(j, W):
                    if i == k and j == l:
                        continue
                    # 从(i,j)到(k,l)的铁路成本
                    cost = A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l))
                    ans = min(ans, cost)
    print(ans)
