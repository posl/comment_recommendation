def is_light_on(s, t, x):
    if s < t:
        return s < x and x < t
    else:
        return s < x or x < t

if __name__ == '__main__':
    is_light_on()