def check_convexity(x1, y1, x2, y2, x3, y3, x4, y4):
    # check if 1-2-3 are clockwise
    # check if 2-3-4 are clockwise
    # check if 3-4-1 are clockwise
    # check if 4-1-2 are clockwise
    # if all of the above are true, then convex
    # if any of the above are false, then concave
    # check 1-2-3
    # 1
    # 2
    # 3
    # 1-2 = (x2-x1, y2-y1)
    # 2-3 = (x3-x2, y3-y2)
    # 1-2 dot 2-3 = (x2-x1)*(x3-x2) + (y2-y1)*(y3-y2)
    # if 1-2 dot 2-3 > 0, then clockwise
    # if 1-2 dot 2-3 < 0, then counter-clockwise
    # if 1-2 dot 2-3 = 0, then colinear
    # 1-2 dot 2-3 = (x2-x1)*(x3-x2) + (y2-y1)*(y3-y2)
    # 2-3 dot 3-4 = (x3-x2)*(x4-x3) + (y3-y2)*(y4-y3)
    # 3-4 dot 4-1 = (x4-x3)*(x1-x4) + (y4-y3)*(y1-y4)
    # 4-1 dot 1-2 = (x1-x4)*(x2-x1) + (y1-y4)*(y2-y1)
    a = (x2-x1)*(y3-y2) + (y2-y1)*(x3-x2)
    b = (x3-x2)*(y4-y3) + (y3-y2)*(x4-x3)
    c = (x4-x3)*(y1-y4) + (y4-y3)*(x1-x4)
    d = (x1-x4)*(y2-y1) + (y1-y

if __name__ == '__main__':
    check_convexity()