def dist( point1, point2 ):
    return sum( (x-y)**2 for x, y in zip(point1, point2) )**0.5
