def main():
    a, b, d = map(int, input().split())
    import math
    rad = math.radians(d)
    import numpy as np
    x = np.array([a, b])
    rotate_matrix = np.array([[math.cos(rad), -math.sin(rad)], [math.sin(rad), math.cos(rad)]])
    y = np.dot(rotate_matrix, x)
    print(y[0], y[1])
