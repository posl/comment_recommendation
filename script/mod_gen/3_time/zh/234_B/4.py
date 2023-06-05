def distance(i,j):
    x = abs(i[0]-j[0])
    y = abs(i[1]-j[1])
    return (x**2+y**2)**0.5

if __name__ == '__main__':
    distance()