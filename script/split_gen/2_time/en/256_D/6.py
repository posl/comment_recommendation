def main():
    N = int(input())
    intervals = []
    for i in range(N):
        intervals.append(list(map(int, input().split())))
    intervals.sort()
    ans = []
    for i in range(N):
        if ans == []:
            ans.append(intervals[i])
        else:
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
    for a in ans:
        print(a[0], a[1])
