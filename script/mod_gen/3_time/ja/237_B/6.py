def main():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(H)]
    for i in range(W):
        print(*[A[j][i] for j in range(H)])
    return

if __name__ == '__main__':
    main()