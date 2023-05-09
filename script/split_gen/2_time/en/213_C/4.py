def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = list(set(A))
    B = list(set(B))
    A.sort()
    B.sort()
    ans = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(N):
        ans[A.index(A[i])][B.index(B[i])] = i + 1
    for i in range(H):
        for j in range(W):
            if ans[i][j] != 0:
                print(A.index(A[ans[i][j] - 1]) + 1, B.index(B[ans[i][j] - 1]) + 1)
