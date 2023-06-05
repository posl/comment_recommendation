def find_max_bridge(bridge_list):
    max_bridge = 0
    for i in range(len(bridge_list)):
        if bridge_list[i] > max_bridge:
            max_bridge = bridge_list[i]
    return max_bridge

if __name__ == '__main__':
    find_max_bridge()