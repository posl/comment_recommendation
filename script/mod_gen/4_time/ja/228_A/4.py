def check_light_on(s, t, x):
    if s < t:
        if s <= x and x < t:
            return True
        else:
            return False
    else:
        if s <= x or x < t:
            return True
        else:
            return False

if __name__ == '__main__':
    check_light_on()