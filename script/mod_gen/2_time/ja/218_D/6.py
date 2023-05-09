def main():
    N = int(input())
    point = [list(map(int,input().split())) for _ in range(N)]
    point.sort()
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            x = point[j][0] - point[i][0]
            y = point[j][1] - point[i][1]
            for k in range(j+1,N):
                if point[k][0] == point[i][0] + y and point[k][1] == point[i][1] - x:
                    for l in range(k+1,N):
                        if point[l][0] == point[j][0] + y and point[l][1] == point[j][1] - x:
                            ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()