def manhattan_distance(x):
    sum = 0
    for i in x:
        sum += abs(i)
    return sum

if __name__ == '__main__':
    manhattan_distance()