def highest_bridge(bridge_heights):
    return bridge_heights.index(max(bridge_heights)) + 1

if __name__ == '__main__':
    highest_bridge()