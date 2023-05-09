def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_num = 100000000
    for i in range(H):
        for j in range(W):
            if A[i][j] < min_num:
                min_num = A[i][j]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min_num
    print(ans)
