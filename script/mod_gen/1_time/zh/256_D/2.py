def main():
    n = int(input())
    intervals = []
    for i in range(n):
        l, r = map(int, input().split())
        intervals.append((l, r))
    intervals.sort()
    l, r = intervals[0]
    for i in range(1, n):
        if intervals[i][0] <= r:
            r = max(intervals[i][1], r)
        else:
            print(l, r)
            l, r = intervals[i]
    print(l, r)

if __name__ == '__main__':
    main()