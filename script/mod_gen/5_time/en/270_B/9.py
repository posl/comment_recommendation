def calc_distance(x,y,z):
    if x > y and y > z:
        return x - z
    else:
        return -1

if __name__ == '__main__':
    calc_distance()