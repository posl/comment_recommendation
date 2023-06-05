def get_distance(x, y):
    return sum([(x[i]-y[i])**2 for i in range(len(x))])**0.5
