def manhattan_distance(x):
    sum = 0
    for i in range(len(x)):
        sum += abs(x[i])
    return sum

if __name__ == '__main__':
    manhattan_distance()