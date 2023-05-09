def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for i in range(W):
        for j in range(H):
            if j == H-1:
                print(A[j][i], end="")
            else:
                print(A[j][i], end=" ")
        print()
