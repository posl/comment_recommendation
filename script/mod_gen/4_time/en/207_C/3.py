def solve():
    N = int(input())
    intervals = []
    for i in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            intervals.append((l, r))
        elif t == 2:
            intervals.append((l, r - 0.1))
        elif t == 3:
            intervals.append((l + 0.1, r))
        elif t == 4:
            intervals.append((l + 0.1, r - 0.1))
    intervals.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if intervals[i][1] >= intervals[j][0]:
                ans += 1
    print(ans)
solve()

if __name__ == '__main__':
    solve()