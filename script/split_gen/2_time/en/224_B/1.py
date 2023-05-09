def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 'Yes'
    for i in range(H):
        for j in range(W):
            if i == H - 1 and j == W - 1:
                continue
            elif i == H - 1:
                if A[i][j] > A[i][j + 1]:
                    ans = 'No'
                    break
            elif j == W - 1:
                if A[i][j] > A[i + 1][j]:
                    ans = 'No'
                    break
            else:
                if A[i][j] > A[i][j + 1] or A[i][j] > A[i + 1][j]:
                    ans = 'No'
                    break
        else:
            continue
        break
    print(ans)
