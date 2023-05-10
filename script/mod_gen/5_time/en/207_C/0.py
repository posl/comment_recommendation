def main():
    N = int(input())
    intervals = []
    for i in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            intervals.append([l, r])
        elif t == 2:
            intervals.append([l, r-1])
        elif t == 3:
            intervals.append([l+1, r])
        elif t == 4:
            intervals.append([l+1, r-1])
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if intervals[i][0] <= intervals[j][0] <= intervals[i][1]:
                ans += 1
            elif intervals[j][0] <= intervals[i][0] <= intervals[j][1]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()