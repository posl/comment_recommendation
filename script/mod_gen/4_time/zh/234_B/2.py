def get_max_distance(coordinates):
    max_distance = 0
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            distance = ((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)**0.5
            if distance > max_distance:
                max_distance = distance
    return max_distance

if __name__ == '__main__':
    get_max_distance()