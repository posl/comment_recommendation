def min_height_stools(people_heights):
    stool_heights = [0] * len(people_heights)
    stool_heights[0] = people_heights[0]
    for i in range(1, len(people_heights)):
        if people_heights[i] > stool_heights[i-1]:
            stool_heights[i] = stool_heights[i-1] + 1
        else:
            stool_heights[i] = people_heights[i]
    return sum(stool_heights) - sum(people_heights)
