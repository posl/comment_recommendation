def main():
    N, D = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        if XY[i][0]**2 + XY[i][1]**2 <= D**2:
            count += 1
    print(count)

if __name__ == '__main__':
    main()