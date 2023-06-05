def solve(n, ranges):
    # write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    total = 0
    for i in range(n):
        total += (ranges[i][1] - ranges[i][0] + 1) * (ranges[i][1] + ranges[i][0]) / 2
    return int(total)
n = int(input())
ranges = []
for _ in range(n):
    ranges.append(list(map(int, input().split())))
print(solve(n, ranges))
