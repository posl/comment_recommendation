def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    for i in range(H1):
        for j in range(W1):
            if A[i][j] in [b for a in B for b in a]:
                B[B.index([b for a in B for b in a if a == A[i][j]])//W2][B.index([b for a in B for b in a if a == A[i][j]])%W2] = 0
    if 0 in [b for a in B for b in a]:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()