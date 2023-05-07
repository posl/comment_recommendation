def main():
    N = int(input())
    intervals = []
    for _ in range(N):
        L, R = map(int, input().split())
        intervals.append((L, R))
    intervals.sort(key=lambda x: x[0])
    ans = []
    L, R = intervals[0]
    for i in range(1, N):
        if R < intervals[i][0]:
            ans.append((L, R))
            L, R = intervals[i]
        else:
            R = max(R, intervals[i][1])
    ans.append((L, R))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
