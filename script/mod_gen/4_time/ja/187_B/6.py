def main():
    N = int(input())
    point_list = []
    for i in range(N):
        x, y = map(int, input().split())
        point_list.append((x, y))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if point_list[i][0] == point_list[j][0]:
                continue
            if -1 <= (point_list[i][1] - point_list[j][1]) / (point_list[i][0] - point_list[j][0]) <= 1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()