def solve():
    N = int(input())
    intervals = []
    for _ in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            intervals.append((l, r))
        elif t == 2:
            intervals.append((l, r - 0.1))
        elif t == 3:
            intervals.append((l + 0.1, r))
        else:
            intervals.append((l + 0.1, r - 0.1))
    intervals.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if intervals[j][0] <= intervals[i][1]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    solve()