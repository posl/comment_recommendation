def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for j in range(W):
        for i in range(H):
            print(A[i][j], end="")
            if i!=H-1:
                print(" ", end="")
            else:
                print()
    return
