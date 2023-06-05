def find_way(from_city, to_city, roads):
    if from_city == to_city:
        return 0
    min_time = 0
    for road in roads:
        if road[0] == from_city:
            next_city = road[1]
            time = find_way(next_city, to_city, roads)
            if time != 0:
                if min_time == 0 or min_time > time + 1:
                    min_time = time + 1
    return min_time

if __name__ == '__main__':
    find_way()