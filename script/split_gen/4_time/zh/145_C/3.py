def get_average_length(N, cities):
    import math
    import itertools
    total_length = 0
    num_of_paths = 0
    for path in itertools.permutations(cities):
        num_of_paths += 1
        for i in range(N-1):
            total_length += math.sqrt((path[i][0] - path[i+1][0])**2 + (path[i][1] - path[i+1][1])**2)
    return total_length/num_of_paths
