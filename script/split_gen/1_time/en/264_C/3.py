def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    print('Yes' if all(B[i][j] <= A[i][j] for i in range(H2) for j in range(W2)) else 'No')
