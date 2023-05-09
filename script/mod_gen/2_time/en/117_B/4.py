def can_draw_polygon(sides):
    sides.sort()
    longest_side = sides.pop()
    if longest_side < sum(sides):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    can_draw_polygon()