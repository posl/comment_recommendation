def main():
    N = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += ((XY[i][0]-XY[j][0])**2+(XY[i][1]-XY[j][1])**2)**0.5
    print(ans*2/N)

if __name__ == '__main__':
    main()