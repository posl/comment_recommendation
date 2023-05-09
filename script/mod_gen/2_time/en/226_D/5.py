def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = set()
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = XY[i]
            x2, y2 = XY[j]
            S.add((x2-x1, y2-y1))
            S.add((x1-x2, y1-y2))
    print(len(S))

if __name__ == '__main__':
    main()