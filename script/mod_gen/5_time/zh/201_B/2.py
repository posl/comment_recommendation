def getSecondHeight(heights):
    heights.sort(reverse=True)
    return heights[1]

if __name__ == '__main__':
    getSecondHeight()