def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    for j in range(W):
        for i in range(H):
            if i != H - 1:
                print(A[i][j], end = " ")
            else:
                print(A[i][j], end = "\n")
