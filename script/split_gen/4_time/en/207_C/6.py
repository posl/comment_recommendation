def main():
    N = int(input())
    intervals = []
    for _ in range(N):
        t, l, r = map(int, input().split())
        interval = [l, r]
        if t == 2 or t == 4:
            interval[1] -= 0.1
        if t == 3 or t == 4:
            interval[0] += 0.1
        intervals.append(interval)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if intervals[i][0] <= intervals[j][0] <= intervals[i][1]:
                ans += 1
            elif intervals[i][0] <= intervals[j][1] <= intervals[i][1]:
                ans += 1
            elif intervals[j][0] <= intervals[i][0] <= intervals[j][1]:
                ans += 1
            elif intervals[j][0] <= intervals[i][1] <= intervals[j][1]:
                ans += 1
    print(ans)
