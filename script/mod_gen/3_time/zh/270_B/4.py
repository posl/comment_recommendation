def get_distance(x, y, z):
    if x < z:
        return -1
    return x - z + y

if __name__ == '__main__':
    get_distance()