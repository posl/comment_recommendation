def main():
    N = int(input())
    intervals = []
    for i in range(N):
        L, R = map(int, input().split())
        intervals.append([L, R])
    intervals.sort(key=lambda x: x[0])
    ans = []
    ans.append(intervals[0])
    for i in range(1, N):
        if ans[-1][1] < intervals[i][0]:
            ans.append(intervals[i])
        elif ans[-1][1] < intervals[i][1]:
            ans[-1][1] = intervals[i][1]
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
