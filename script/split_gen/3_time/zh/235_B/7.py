def find_last_platform_height(n, heights):
    last_platform_height = 0
    for i in range(n-1):
        if heights[i] < heights[i+1]:
            last_platform_height = heights[i+1]
    return last_platform_height
