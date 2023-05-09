def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    if H1 < H2 or W1 < W2:
        print("No")
        return
    for i in range(H1-H2+1):
        for j in range(W1-W2+1):
            if sum([A[i+k][j:j+W2] for k in range(H2)], []) == sum(B, []):
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()