def get_min_distance(shrines, temples, x):
    min_distance = float('inf')
    for shrine in shrines:
        for temple in temples:
            distance = abs(shrine - x) + abs(temple - shrine)
            if distance < min_distance:
                min_distance = distance
    return min_distance

if __name__ == '__main__':
    get_min_distance()