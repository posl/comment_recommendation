def main():
    # get input
    a, b, x = map(int, input().split())
    # calculate
    if x <= a*a*b/2:
        # when x is less than half of the volume, the angle is 90 degrees minus the angle of the triangle
        angle = 90 - math.degrees(math.atan(2*x/a/b/b))
    else:
        # when x is more than half of the volume, the angle is the angle of the triangle
        angle = math.degrees(math.atan(2*(a*a*b-x)/a/a/a))
    # output
    print(angle)

if __name__ == '__main__':
    main()