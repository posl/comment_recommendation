def can_draw_polygon(sides):
    sides.sort()
    longest_side = sides.pop()
    if longest_side < sum(sides):
        return "Yes"
    else:
        return "No"
