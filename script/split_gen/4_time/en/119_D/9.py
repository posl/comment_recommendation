def get_distance_from_shrine(shrine, shrine_list):
    left = 0
    right = len(shrine_list) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if shrine_list[mid] == shrine:
            return 0
        elif shrine_list[mid] < shrine:
            left = mid + 1
        else:
            right = mid - 1
    if right < 0:
        return shrine_list[0] - shrine
    if left >= len(shrine_list):
        return shrine - shrine_list[-1]
    return min(shrine_list[left] - shrine, shrine - shrine_list[right])
