def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i == 0:
                if j == 0:
                    continue
                else:
                    A[i][j] += A[i][j-1]
            else:
                if j == 0:
                    A[i][j] += A[i-1][j]
                else:
                    A[i][j] += A[i][j-1] + A[i-1][j] - A[i-1][j-1]
    for i in range(H):
        for j in range(W):
            if i == 0:
                if j == 0:
                    continue
                else:
                    if A[i][j] <= A[i][j-1]:
                        print('No')
                        return
            else:
                if j == 0:
                    if A[i][j] <= A[i-1][j]:
                        print('No')
                        return
                else:
                    if A[i][j] <= A[i-1][j] + A[i][j-1] - A[i-1][j-1]:
                        print('No')
                        return
    print('Yes')
