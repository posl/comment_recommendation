def main():
    # Get the number of intervals
    num_intervals = int(input())
    # Get the intervals
    intervals = []
    for i in range(num_intervals):
        interval = input().split()
        interval = [int(x) for x in interval]
        intervals.append(interval)
    # Sort the intervals by the first value
    intervals.sort(key=lambda x: x[0])
    # Go through the intervals and merge them if they overlap
    merged_intervals = []
    current_interval = intervals[0]
    for i in range(1, num_intervals):
        if intervals[i][0] <= current_interval[1]:
            # The intervals overlap, so merge them
            current_interval[1] = max(current_interval[1], intervals[i][1])
        else:
            # The intervals don't overlap, so add the current interval to the list of merged intervals
            merged_intervals.append(current_interval)
            current_interval = intervals[i]
    # Add the last interval to the list of merged intervals
    merged_intervals.append(current_interval)
    # Print the number of merged intervals
    print(len(merged_intervals))
    # Print the merged intervals
    for interval in merged_intervals:
        print(interval[0], interval[1])

if __name__ == '__main__':
    main()