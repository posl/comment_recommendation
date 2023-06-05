def get_distance(x, y):
    result = 0
    for i in range(len(x)):
        result += (x[i]-y[i])**2
    return result**0.5

if __name__ == '__main__':
    get_distance()