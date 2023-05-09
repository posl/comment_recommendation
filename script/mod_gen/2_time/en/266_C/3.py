def getAngle(a, b, c):
    ab = (a[0] - b[0], a[1] - b[1])
    bc = (b[0] - c[0], b[1] - c[1])
    dot = ab[0] * bc[0] + ab[1] * bc[1]
    cross = ab[0] * bc[1] - ab[1] * bc[0]
    alpha = math.atan2(cross, dot)
    return alpha

if __name__ == '__main__':
    getAngle()