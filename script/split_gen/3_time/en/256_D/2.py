def main():
    n = int(input())
    intervals = []
    for _ in range(n):
        l, r = map(int, input().split())
        intervals.append((l, r))
    intervals.sort()
    ans = []
    for l, r in intervals:
        if not ans or ans[-1][1] < l:
            ans.append((l, r))
        else:
            ans[-1] = (ans[-1][0], max(ans[-1][1], r))
    for l, r in ans:
        print(l, r)
