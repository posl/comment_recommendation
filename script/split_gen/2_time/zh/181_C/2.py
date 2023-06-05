def sumOfIntervals(intervals):
    sum = 0
    for interval in intervals:
        sum += interval[1] - interval[0] + 1
    return sum
