def is_light(s, t, x):
    if s < t:
        return s <= x and x < t
    else:
        return s <= x or x < t
