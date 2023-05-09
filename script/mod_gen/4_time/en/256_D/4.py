def main():
    n = int(input())
    intervals = []
    for i in range(n):
        intervals.append(list(map(int, input().split())))
    intervals.sort(key=lambda x: x[0])
    result = []
    result.append(intervals[0])
    for i in range(1, n):
        if intervals[i][0] < result[-1][1]:
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append(intervals[i])
    for i in range(len(result)):
        print(result[i][0], result[i][1])

if __name__ == '__main__':
    main()