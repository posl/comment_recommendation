def get_median(heights, k):
    n = len(heights)
    # 1. get the sum of the first k*k elements
    sum = 0
    for i in range(k):
        for j in range(k):
            sum += heights[i][j]
    # 2. get the median
    median = (k*k)//2 + 1
    # 3. get the median of the first k*k elements
    median_value = 0
    for i in range(k):
        for j in range(k):
            median_value += heights[i][j]
            if median_value >= median:
                return heights[i][j]
    # 4. get the median of the first k*k elements
    median_value = 0
    for i in range(k):
        for j in range(k):
            median_value += heights[j][i]
            if median_value >= median:
                return heights[j][i]
    return 0

if __name__ == '__main__':
    get_median()