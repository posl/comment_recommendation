def func():
    n = int(input())
    intervals = []
    for i in range(n):
        t, l, r = map(int, input().split())
        intervals.append((t, l, r))
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if intervals[i][1] <= intervals[j][1] <= intervals[i][2] or intervals[i][1] <= intervals[j][2] <= intervals[i][2] or intervals[j][1] <= intervals[i][1] <= intervals[j][2] or intervals[j][1] <= intervals[i][2] <= intervals[j][2]:
                count += 1
    print(count)
func()

if __name__ == '__main__':
    func()