def main():
    N = int(input())
    intervals = [list(map(int, input().split())) for _ in range(N)]
    intervals.sort()
    ans = []
    for i in range(N):
        if i == 0:
            ans.append(intervals[i])
        else:
            if ans[-1][1] >= intervals[i][1]:
                continue
            elif ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = intervals[i][1]
            else:
                ans.append(intervals[i])
    for a in ans:
        print(*a)

if __name__ == '__main__':
    main()