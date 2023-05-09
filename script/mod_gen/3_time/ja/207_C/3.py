def main():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if data[i][0] == 1:
                l = data[i][1]
            else:
                l = data[i][1]+1
            if data[i][0] == 3:
                r = data[i][2]
            else:
                r = data[i][2]-1
            if data[j][0] == 1:
                l2 = data[j][1]
            else:
                l2 = data[j][1]+1
            if data[j][0] == 3:
                r2 = data[j][2]
            else:
                r2 = data[j][2]-1
            if l <= r2 and l2 <= r:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()