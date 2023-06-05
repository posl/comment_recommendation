def findLastPlatform(heights):
    lastPlatform = heights[0]
    for i in range(1, len(heights)):
        if heights[i] > lastPlatform:
            lastPlatform = heights[i]
    return lastPlatform
