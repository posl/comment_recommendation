def lattice_point(x1, y1, x2, y2):
    if (x1 == x2 and y1 == y2):
        return "No"
    #check if (x1, y1) is a lattice point
    if ((x1**2 + y1**2)**0.5).is_integer():
        return "Yes"
    #check if (x2, y2) is a lattice point
    if ((x2**2 + y2**2)**0.5).is_integer():
        return "Yes"
    #if (x1, y1) and (x2, y2) are both lattice points, then a point (x, y) is a lattice point if and only if
    #x = x1 + a(x2 - x1) and y = y1 + a(y2 - y1) where a is an integer
    #if (x1, y1) and (x2, y2) are not both lattice points, then a point (x, y) is a lattice point if and only if
    #x = x1 + a(x2 - x1) and y = y1 + a(y2 - y1) where a is an integer and a is not 0
    #if a is 0, then (x, y) = (x1, y1) or (x, y) = (x2, y2)
    #if a is not 0, then (x, y) = (x1, y1) + a(x2 - x1, y2 - y1)
    #if (x1, y1) is a lattice point, then (x1, y1) + a(x2 - x1, y2 - y1) is a lattice point
    #if (x2, y2) is a lattice point, then (x1, y1) + a(x2 - x1, y2 - y1) is a lattice point
    #if (x1, y1) and (x2, y2) are both not lattice points, then (x1, y1) + a(x2 - x1, y2 - y1) is a lattice point
    #if (x1, y1) and (x2, y2) are both not lattice points
