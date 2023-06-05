def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_A = min([min(A[i]) for i in range(H)])
    print(sum([sum([A[i][j] - min_A for j in range(W)]) for i in range(H)]))
