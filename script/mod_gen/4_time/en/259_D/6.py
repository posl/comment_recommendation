def is_inside_circle(circle, point):
    x = circle[0]
    y = circle[1]
    r = circle[2]
    x1 = point[0]
    y1 = point[1]
    if ((x1-x)**2 + (y1-y)**2) <= r**2:
        return True
    return False

if __name__ == '__main__':
    is_inside_circle()