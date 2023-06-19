def get_max_bridge(bridge_heights):
    max_height = 0
    max_index = 0
    for i in range(0, len(bridge_heights)):
        if bridge_heights[i] > max_height:
            max_height = bridge_heights[i]
            max_index = i + 1
    return max_index
