def can_draw_polygons(sides):
    sides.sort()
    if sides[-1] < sum(sides[:-1]):
        return "Yes"
    else:
        return "No"
