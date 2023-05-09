def main():
    n = int(input())
    intervals = []
    for _ in range(n):
        intervals.append([int(x) for x in input().split()])
    intervals.sort()
    ans = []
    for i in range(n):
        if len(ans) == 0:
            ans.append(intervals[i])
            continue
        if ans[-1][1] < intervals[i][0]:
            ans.append(intervals[i])
        else:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

if __name__ == '__main__':
    main()