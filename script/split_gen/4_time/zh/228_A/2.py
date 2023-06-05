def is_light_on(s, t, x):
    if s < t:
        if s < x and x < t:
            return True
        else:
            return False
    else:
        if t < x and x < s:
            return False
        else:
            return True
