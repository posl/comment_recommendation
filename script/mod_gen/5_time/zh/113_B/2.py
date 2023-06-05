def get_index(temperature,altitude):
    min = 100000000
    index = 0
    for i in range(len(altitude)):
        if abs(temperature - (altitude[i] * 0.006)) < min:
            min = abs(temperature - (altitude[i] * 0.006))
            index = i
    return index + 1

if __name__ == '__main__':
    get_index()