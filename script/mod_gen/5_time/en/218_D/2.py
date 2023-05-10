def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    xy.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if xy[i][0] < xy[j][0] and xy[i][1] < xy[j][1]:
                if [xy[i][0], xy[j][1]] in xy and [xy[j][0], xy[i][1]] in xy:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()