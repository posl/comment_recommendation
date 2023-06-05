def check(heights):
    heights.sort()
    for i in range(len(heights)-1):
        if heights[i+1] - heights[i] > 1:
            return False
    return True
