def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    print(sum([sum(A[i]) for i in range(H)])-min([min(A[i]) for i in range(H)])*H*W)

if __name__ == '__main__':
    main()