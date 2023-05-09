def main():
    import sys
    input = sys.stdin.readline
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    ans = "Yes"
    for i in range(H1):
        for j in range(W1):
            if i < H2 and j < W2:
                if A[i][j] != B[i][j]:
                    ans = "No"
                    break
            else:
                if A[i][j] != 0:
                    ans = "No"
                    break
    print(ans)
