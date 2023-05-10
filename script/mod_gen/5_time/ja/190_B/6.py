def main():
    N, S, D = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        if XY[i][0] < S and XY[i][1] > D:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()