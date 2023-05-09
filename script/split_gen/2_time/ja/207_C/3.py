def main():
    N = int(input())
    ranges = []
    for _ in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            ranges.append((l, r))
        elif t == 2:
            ranges.append((l, r - 1))
        elif t == 3:
            ranges.append((l + 1, r))
        else:
            ranges.append((l + 1, r - 1))
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if ranges[i][0] <= ranges[j][1] and ranges[j][0] <= ranges[i][1]:
                ans += 1
    print(ans)
