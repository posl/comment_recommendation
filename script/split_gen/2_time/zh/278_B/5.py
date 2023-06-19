def get_next_time(h,m):
    next_h = h
    next_m = m
    while True:
        if next_m == 59:
            next_m = 0
            if next_h == 23:
                next_h = 0
            else:
                next_h += 1
        else:
            next_m += 1
        if is_confused_time(next_h,next_m):
            return next_h,next_m
