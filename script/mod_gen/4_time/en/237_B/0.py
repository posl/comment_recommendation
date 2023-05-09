def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [[A[j][i] for j in range(H)] for i in range(W)]
    for i in range(W):
        print(*B[i])

if __name__ == '__main__':
    main()