def union_intervals(intervals):
    intervals.sort()
    union = []
    for interval in intervals:
        if not union or union[-1][1] < interval[0]:
            union.append(interval)
        else:
            union[-1][1] = max(union[-1][1], interval[1])
    return union
