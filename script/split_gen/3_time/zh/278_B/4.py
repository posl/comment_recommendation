def get_next_time(time):
    h = time[0]
    m = time[1]
    while True:
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0
        if is_confused_time([h, m]):
            return [h, m]
