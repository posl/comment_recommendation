def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i < k and j < l:
                        if A[i][j] + A[k][l] > A[k][j] + A[i][l]:
                            print('No')
                            exit()
    print('Yes')
