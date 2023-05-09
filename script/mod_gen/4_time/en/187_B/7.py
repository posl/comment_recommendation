def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(tuple(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (points[i][1]-points[j][1])/(points[i][0]-points[j][0]) <= 1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()