def find_ways_to_make_triangles(stick_lengths):
    stick_lengths.sort()
    ways = 0
    for i in range(len(stick_lengths)):
        for j in range(i + 1, len(stick_lengths)):
            for k in range(j + 1, len(stick_lengths)):
                if stick_lengths[i] + stick_lengths[j] > stick_lengths[k]:
                    ways += 1
    return ways
