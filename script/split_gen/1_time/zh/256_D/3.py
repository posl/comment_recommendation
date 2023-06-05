def merge_intervals(intervals):
    # 先排序
    intervals.sort(key=lambda x: x[0])
    # print(intervals)
    merged = []
    for interval in intervals:
        # 如果列表为空，或者当前区间与上一区间不重合，直接添加
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
            # 否则的话，我们就可以与上一区间进行合并
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
