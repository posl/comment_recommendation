def format_time(time):
    if time < 10:
        return '0' + str(time)
    else:
        return str(time)
