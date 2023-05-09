def main():
    N, M = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    L = [LR[i][0] for i in range(M)]
    R = [LR[i][1] for i in range(M)]
    print(max(0, min(R) - max(L) + 1))

if __name__ == '__main__':
    main()