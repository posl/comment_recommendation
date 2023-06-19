def get_distance(ropes):
    total_length = 0
    for rope in ropes:
        total_length += rope[0]
    total_time = total_length
    for rope in ropes:
        total_time += rope[0]/rope[1]
    return total_length/2.0
