def main():
    # Get the number of intervals.
    n = int(input())
    # Create a list of intervals.
    intervals = []
    for i in range(n):
        # Get the interval.
        interval = input().split(' ')
        # Append the interval to the list of intervals.
        intervals.append((int(interval[0]), int(interval[1])))
    # Sort the intervals by their left end.
    intervals.sort(key=lambda tup: tup[0])
    # Initialize the list of merged intervals.
    merged_intervals = []
    # Initialize the first interval.
    merged_intervals.append(intervals[0])
    # Iterate through the intervals.
    for i in range(1, n):
        # Get the current interval.
        current_interval = intervals[i]
        # Get the last interval in the list of merged intervals.
        last_interval = merged_intervals[-1]
        # Check if the current interval and the last interval overlap.
        if current_interval[0] >= last_interval[0] and current_interval[0] < last_interval[1]:
            # Check if the current interval is longer than the last interval.
            if current_interval[1] > last_interval[1]:
                # Update the last interval.
                merged_intervals[-1] = (last_interval[0], current_interval[1])
        else:
            # Append the current interval to the list of merged intervals.
            merged_intervals.append(current_interval)
    # Iterate through the merged intervals.
    for i in range(len(merged_intervals)):
        # Get the merged interval.
        merged_interval = merged_intervals[i]
        # Print the merged interval.
        print(merged_interval[0], merged_interval[1])

if __name__ == '__main__':
    main()