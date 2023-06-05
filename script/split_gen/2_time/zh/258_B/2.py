def print_time(k):
    start_time = 21 * 60
    end_time = start_time + 100
    k_time = start_time + k
    if k_time < end_time:
        hour = k_time // 60
        minute = k_time % 60
        print("%02d:%02d" % (hour, minute))
    else:
        print("00:00")
