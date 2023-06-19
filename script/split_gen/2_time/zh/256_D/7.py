def merge_intervals(intervals):
    intervals.sort()
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
n = int(input())
intervals = []
for i in range(n):
    intervals.append(list(map(int, input().split())))
merged = merge_intervals(intervals)
for interval in merged:
    print(interval[0], interval[1])
