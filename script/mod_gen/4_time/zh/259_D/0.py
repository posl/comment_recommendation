def is_in_circle(x, y, circles):
    for circle in circles:
        if (x-circle[0])**2 + (y-circle[1])**2 <= circle[2]**2:
            return True
    return False

if __name__ == '__main__':
    is_in_circle()