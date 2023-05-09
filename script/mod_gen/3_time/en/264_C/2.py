def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    print("Yes" if H1 >= H2 and W1 >= W2 and all([all([A[i][j] >= B[i][j] for j in range(W2)]) for i in range(H2)]) else "No")

if __name__ == '__main__':
    main()