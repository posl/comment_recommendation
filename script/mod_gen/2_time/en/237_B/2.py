def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    for i in range(W):
        for j in range(H):
            print(A[j][i], end = ' ')
        print()
main()

if __name__ == '__main__':
    main()