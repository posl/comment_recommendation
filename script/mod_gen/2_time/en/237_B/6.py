def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    for i in range(W):
        print(' '.join(map(str, [A[j][i] for j in range(H)])))

if __name__ == '__main__':
    main()