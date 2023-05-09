def main():
    N = int(input())
    intervals = []
    for _ in range(N):
        l, r = map(int, input().split())
        intervals.append((l, r))
    intervals.sort()
    ans = []
    for i in range(N):
        l, r = intervals[i]
        if ans and ans[-1][1] >= l:
            ans[-1][1] = max(ans[-1][1], r)
        else:
            ans.append([l, r])
    for a in ans:
        print(a[0], a[1])
