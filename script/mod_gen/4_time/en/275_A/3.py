def get_highest_bridge(bridge_heights):
    return bridge_heights.index(max(bridge_heights)) + 1

if __name__ == '__main__':
    get_highest_bridge()