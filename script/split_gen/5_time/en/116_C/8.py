def find_min_watering_ops(N, heights):
    count = 0
    for i in range(1, N):
        if heights[i] > heights[i-1]:
            count += heights[i] - heights[i-1]
    return count
