def main():
    n = int(input())
    intervals = []
    for i in range(n):
        intervals.append([int(x) for x in input().split()])
    intervals.sort(key=lambda x: x[0])
    end = intervals[0][1]
    start = intervals[0][0]
    for i in range(1, n):
        if intervals[i][0] > end:
            print(start, end)
            start = intervals[i][0]
            end = intervals[i][1]
        else:
            end = max(end, intervals[i][1])
    print(start, end)

if __name__ == '__main__':
    main()